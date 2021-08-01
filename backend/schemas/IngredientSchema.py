from config.apps import ma
from models.models import *

class IngredientSchema(ma.Schema):
    class Meta:
        fields = (
            "ingredient_id", 
            "name", 
            "description", 
            "img_url", 
            "measure_number",
            "measure_type",
            "energy",
            "fat",
            "carbohydrate",
            "protien",
            "sodium",
            "create_time", 
            "update_time"
        )

ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)