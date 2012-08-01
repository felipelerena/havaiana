from flask import Flask, render_template
from inspect import getmembers
from ojota import Ojota


def get_ojotines(package):
    hijos = []
    items = getmembers(package)
    for item in items:
        try:
            if item[0] != "Ojota" and issubclass(item[1], Ojota):
                hijos.append(item)
        except TypeError:
            pass
    return hijos

def run(package):
    ojotines = get_ojotines(package)
    app = Flask(__name__)
    classes_map = {}
    for item in ojotines:
        classes_map[item[1].plural_name] = item
        #print item[1].all()

    @app.route("/<name>")
    @app.route("/<name>/<pk>")
    def table(name, pk=None):
        item = classes_map[name]
        cls = item[1]
        if pk is None:
            return render_template('table.html', items=cls.all(),
                                   class_name=name)
        else:
            params = {getattr(cls, "pk_field"): pk}
            item = cls.get(**params)
            attrs = []
            for field in item.fields:
                required = field in item.required_fields
                value = getattr(item, field)
                relation_data = item.relations.get(field)
                if value is None or relation_data is None:
                    related = False
                else:
                    related = "/%s/%s" % (relation_data[0].plural_name, value)
                attrs.append((field, value, required, related))

            return render_template('item.html', item=item, attrs=attrs,
                                   class_name=name)

    @app.route('/')
    def index():
        return render_template('tables.html', classes=classes_map.keys())

    app.debug = True
    app.run()

