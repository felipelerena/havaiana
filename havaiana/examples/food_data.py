from ojota import Ojota, Relation


class RecipeType(Ojota):
    plural_name = "Recipe Types"
    required_fields = ("name", )

    def __repr__(self):
        return self.name


class Recipe(Ojota):
    plural_name = "Recipes"
    required_fields = ("name", "instructions")
    recipe_type = Relation("type_id", RecipeType, "recipes")
    data_in_root = False
    def __repr__(self):
        return self.name


class Ingredient(Ojota):
    plural_name = "Ingredients"
    required_fields = ("name", )
    recipe = Relation("recipe_id", Recipe, "ingredients")
    data_in_root = False

    def __repr__(self):
        return self.name


class RecipesByDay(Ojota):
    plural_name = "Recipes uploaded by day"
    pk_field = "date"
    required_fields = ("number", )
    default_order = "date"

    def __repr__(self):
        return self.date
