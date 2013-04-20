import food_data

from havaiana import Site
from havaiana.charts import LineChart

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


class RainChartView(LineChart):
    def __init__(self):
       LineChart.__init__(self, "Recipes uploaded to the site",
                          "uploads", 800, 400)

    def get_data(self, data):
        keys = []
        points = []
        for element in data:
            keys.append(element.date)
            points.append({"value": int(element.number),
                           "xlink": "/Recipes uploaded by day/%s" % element.date})
        return keys, points

if __name__ == "__main__":
    renderers = [
        ('Recipe', 'ingredients', ingredients_list),
        ('RecipesByDay', "__index_chart", RainChartView)
    ]

    site = Site(food_data, "My Food Database", renderers)
    site.serve()
