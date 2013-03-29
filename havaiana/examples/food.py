import food_data

from havaiana import Site

def ingredients_list(field, item, backwards):
    required = field in item.required_fields
    ingredients = getattr(item, field)
    items = []
    for element in ingredients:
        item = '<li><a href="/Ingredients/%s">%s</a></li>' % (element.primary_key,
                                                     element)
        items.append(item)
    value = "<ul>%s</ul>" %  "".join(items)
    related = False

    return (field, value, required, related)

if __name__ == "__main__":
    renderers = [('Recipe', 'ingredients', ingredients_list)]

    site = Site(food_data, "My Food Database", renderers)
    site.serve()



