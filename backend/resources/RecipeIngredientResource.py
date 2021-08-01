import json
from schemas.RecipeSchema import *
from schemas.IngredientSchema import Ingredient

from flask_restful import Resource

class RGAddResource(Resource):
    def put(self):
        for data in request.json:
            recipe_ingred = RecipeIngredient.query.filter_by(recipe_id=data["recipe_id"], ingredient_id=data["ingredient_id"]).first() or None
            if not recipe_ingred:
                new_ri = RecipeIngredient(
                    recipe_id = data["recipe_id"], 
                    ingredient_id = data["ingredient_id"],
                    quantity = data["quantity"]
                )
                db.session.add(new_ri)
            else:
                recipe_ingred.quantity = int(data['quantity'])
            db.session.commit()
        return True

    def delete(self):
        rid = request.json['recipe_id']
        iid = request.json['ingredient_id']
        model = RecipeIngredient.query.get_or_404(recipe_id=rid, ingredient_id=iid)
        db.session.delete(model)
        db.session.commit()
        return '', 204