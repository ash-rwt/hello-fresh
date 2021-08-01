from schemas.RecipeSchema import *
from schemas.MenuSchema import Menu

from flask_restful import Resource

class RecipeListResource(Resource):
    def get(self, menu_id):
        recipes = Recipe.query.filter_by(menu_id=menu_id).all()
        return recipes_schema.dump(recipes)

    def post(self, menu_id):
        menu = Menu.query.get_or_404(request.json['menu_id'])
        
        new_recipe = Recipe(
            menu_id     = request.json['menu_id'], 
            name        = request.json['name'],
            description = request.json['description'],
            img_url     = request.json['img_url'],
        )
        db.session.add(new_recipe)
        db.session.commit()
        return recipe_schema.dump(new_recipe)

class RecipeOneResource(Resource):
    def get(self, menu_id, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        return recipe_schema.dump(recipe)

    def patch(self, menu_id, recipe_id):
        Menu.query.get_or_404(request.json['menu_id'])
        recipe = Recipe.query.get_or_404(recipe_id)

        for field in request.json:
            if field in request.json and field != "recipe_id":
                setattr(recipe, field, request.json[field])

        db.session.commit()
        return recipe_schema.dump(recipe)

    def delete(self, menu_id, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
        return '', 204
