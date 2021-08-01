from config.apps import ma
from models.models import *

class RecipeSchema(ma.Schema):
    class Meta:
        fields = ("recipe_id", "menu_id", "name", "description", "img_url", "create_time", "update_time")

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)