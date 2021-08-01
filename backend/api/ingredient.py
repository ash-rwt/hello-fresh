from flask import Blueprint
ingredientApi = Blueprint('ingredientApi', __name__)

@ingredientApi.route("<int:recipeId>/list/", methods=['GET'])
def ingredientList(recipeId):
    return "list of ingreadient by recipe"

@ingredientApi.route("<int:recipeId>/list-by-id/<int:id>/", methods=['GET'])
def ingredientListById(recipeId, id):
    return "list of ingredient"

@ingredientApi.route("<int:recipeId>/add/", methods=['POST'])
def ingredientAdd(recipeId):
    return "Add ingredient"

@ingredientApi.route("<int:recipeId>/update/<int:id>/", methods=['PUT'])
def ingredientUpdate(id):
    return "Update ingredient"

@ingredientApi.route("<int:recipeId>/delete/<int:id>/", methods=['DELETE'])
def ingredientDelete(id):
    return "Delete ingredient"