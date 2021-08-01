import os
import datetime
from flask import Flask
from flask_migrate import Migrate
from config.apps import db, ma, api

app = Flask(__name__)
app.config.from_object('config.config.DevelopmentConfig')

db.init_app(app)
ma.init_app(app)

migrate = Migrate(app, db)

from resources.MenuResource import MenuListResource, MenuOneResource
api.add_resource(MenuListResource, '/api/menus')
api.add_resource(MenuOneResource, '/api/menu/<int:menu_id>')

from resources.RecipeResource import RecipeListResource, RecipeOneResource
api.add_resource(RecipeListResource, '/api/<int:menu_id>/recipies')
api.add_resource(RecipeOneResource, '/api/<int:menu_id>/recipe/<int:recipe_id>')

from resources.InstructionResource import InstructionListResource, InstructionOneResource
api.add_resource(InstructionListResource, '/api/<int:recipe_id>/instructions')
api.add_resource(InstructionOneResource, '/api/<int:recipe_id>/instruction/<int:instruction_id>')

from resources.IngredientResource import IngredientListResource, IngredientOneResource
api.add_resource(IngredientListResource, '/api/ingredients')
api.add_resource(IngredientOneResource, '/api/ingredient/<int:ingredient_id>')

from resources.RecipeIngredientResource import RGAddResource
api.add_resource(RGAddResource, '/api/recipe-ingredient')

api.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7100)