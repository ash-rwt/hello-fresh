from config.apps import ma
from models.models import *

class MenuSchema(ma.Schema):
    class Meta:
        fields = ("menu_id", "name", "description", "rating", "img_url", "create_time", "update_time")

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)