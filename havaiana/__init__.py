from flask import Flask, render_template
from inspect import getmembers
from ojota import Ojota


def get_ojota_children(package):
    hijos = []
    items = getmembers(package)
    for item in items:
        try:
            if item[0] != "Ojota" and issubclass(item[1], Ojota):
                hijos.append(item)
        except TypeError:
            pass
    return hijos

def default_renderer(field, item):
    required = field in item.required_fields
    value = getattr(item, field)
    relation_data = item.relations.get(field)

    if value is None or relation_data is None:
        related = False
    else:
        related = "/%s/%s" % (relation_data[0].plural_name, value)

    return (field, value, required, related)

def render_field(field, item, renderers):
    render = default_renderer
    for renderer in renderers:
        if renderer[0] == field:
            render = renderer[1]

    return render(field, item)

def run(package, renderers=None):
    classes = get_ojota_children(package)
    app = Flask(__name__)
    classes_map = {}
    for item in classes:
        classes_map[item[1].plural_name] = item
        #print item[1].all()

    @app.route("/<name>")
    @app.route("/<name>/<pk>")
    def table(name, pk=None):
        item = classes_map[name]
        cls = item[1]
        class_renderers = [renderer[1:] for renderer in renderers
                           if renderer[0] == item[0]]
        if pk is None:
            return render_template('table.html', items=cls.all(),
                                   class_name=name)
        else:
            params = {getattr(cls, "pk_field"): pk}
            item = cls.get(**params)
            attrs = []
            for field in item.fields:
                attrs.append(render_field(field, item, class_renderers))

            return render_template('item.html', item=item, attrs=attrs,
                                   class_name=name)

    @app.route('/')
    def index():
        return render_template('tables.html', classes=classes_map.keys())

    app.debug = True
    app.run()

