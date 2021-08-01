from schemas.IngredientSchema import *
from flask_restful import Resource

class IngredientListResource(Resource):
    def get(self):
        ingredients = Ingredient.query.all()
        return ingredients_schema.dump(ingredients)

    def post(self):
        new_ingredient = Ingredient(
            name = request.json['name'],
            description = request.json['description'],
            img_url = request.json['img_url'],
            measure_number = request.json['measure_number'],
            measure_type = request.json['measure_type'],
            energy = request.json['energy'],
            fat = request.json['fat'],
            carbohydrate = request.json['carbohydrate'],
            protien = request.json['protien'],
            sodium = request.json['sodium'],
        )
        db.session.add(new_ingredient)
        db.session.commit()
        return ingredient_schema.dump(new_ingredient)


class IngredientOneResource(Resource):
    def get(self, ingredient_id):
        ingredient = Ingredient.query.get_or_404(ingredient_id)
        return ingredient_schema.dump(ingredient)

    def patch(self, ingredient_id):
        ingredient = Ingredient.query.get_or_404(ingredient_id)

        for field in request.json:
            if field in request.json and field != "ingredient_id":

                setattr(ingredient, field, request.json[field])

        db.session.commit()
        return ingredient_schema.dump(ingredient)

    def delete(self, ingredient_id):
        ingredient = Ingredient.query.get_or_404(ingredient_id)
        db.session.delete(ingredient)
        db.session.commit()
        return '', 204
