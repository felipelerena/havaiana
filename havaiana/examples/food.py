import food_data

from havaiana import run

"""
def ingredients_list(field, item):
    required = field in item.required_fields
    ingredients = getattr(item, field)
    items = []
    for element in ingredients:
        item = '<a href="/Ingredients/%s">%s</a>' % (element.primary_key,
                                                     element)
        items.append(item)
    value = ", ".join(items)
    related = False

    return (field, value, required, related)
"""
if __name__ == "__main__":
    # renderers = [('Recipe', 'ingredients', ingredients_list)]
    run(food_data, "My Food Database")
