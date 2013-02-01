import os

from inspect import getmembers
from ojota import Ojota

from flask.helpers import url_for, send_file
from flask import Flask, render_template

from jinja2 import FileSystemLoader
template_path = os.path.join(os.path.dirname(__file__), "templates")

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

def default_renderer(field, item, backwards=False):
    if item.required_fields is not None:
        required = field in item.required_fields
    else:
        required = False
    value = getattr(item, field)
    relation_data = item.relations.get(field)

    if backwards:
        items = []
        for element in value:
            item_ = '<a href="/%s/%s">%s</a>' % (element.plural_name,
                                                element.primary_key,
                                                element)
            items.append(item_)
        value = ", ".join(items)
        related = False
    elif value is None or relation_data is None:
        related = False
    else:
        related = "/%s/%s" % (relation_data[0].plural_name, value)
        value = relation_data[0].get(value)
        field = relation_data[1]

    if field == item.pk_field:
        field = "Primary Key (%s)" % field
    else:
        field = field.replace("_", "  ").capitalize()

    return (field, value, required, related)

def render_field(field, item, renderers, backwards=False):
    render = default_renderer
    for renderer in renderers:
        if renderer[0] == field:
            render = renderer[1]

    return render(field, item, backwards)

def run(package, title="Havaiana", renderers=None):
    if renderers is None:
        renderers  = []
    classes = get_ojota_children(package)
    app = Flask(__name__)
    app.jinja_loader = FileSystemLoader(template_path)

    classes_map = {}
    for item in classes:
        classes_map[item[1].plural_name] = item

    @app.route("/<name>")
    @app.route("/<name>/<pk>")
    def table(name, pk=None):
        item = classes_map[name]
        cls = item[1]
        class_renderers = [renderer[1:] for renderer in renderers
                           if renderer[0] == item[0]]
        if pk is None:
            return render_template('table.html', items=cls.all(),
                                   class_name=name, title=title)
        else:
            params = {getattr(cls, "pk_field"): pk}
            item = cls.get(**params)
            attrs = []
            for field in item.fields:
                attrs.append(render_field(field, item, class_renderers))
            for bw_rel in item.backwards_relations:
                attrs.append(render_field(bw_rel, item, class_renderers, True))

            return render_template('item.html', item=item, attrs=attrs,
                                   class_name=name, title=title)

    @app.route('/media/<path:filename>')
    def custom_static(filename):
        parts = filename.split("/")
        dir_name = "/".join(parts[:-1])
        filename = parts[-1]
        return send_file("templates/static/%s/%s" % (dir_name, filename))

    @app.route('/absolute//<path:filename>')
    def custom_absolute_static(filename):
        parts = filename.split("/")
        dir_name = "/".join(parts[:-1])
        filename = parts[-1]
        print "FILE", dir_name, filename
        return send_file("/%s/%s" % (dir_name, filename))

    @app.route('/')
    def index():
        return render_template("tables.html", classes=classes_map.keys(),
                               title=title)

    app.debug = True
    app.run()

