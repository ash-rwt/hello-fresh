from flask import Blueprint
recipeApi = Blueprint('recipeApi', __name__)

@recipeApi.route("<int:menuId>/list/", methods=['GET'])
def recipeList(menuId):
    return "list of ingreadient by menu"

@recipeApi.route("<int:menuId>/list-by-id/<int:id>/", methods=['GET'])
def recipeListById(menuId, id):
    return "list of recipe"

@recipeApi.route("<int:menuId>/add/", methods=['POST'])
def recipeAdd(menuId):
    return "Add recipe"

@recipeApi.route("<int:menuId>/update/<int:id>/", methods=['PUT'])
def recipeUpdate(menuId, id):
    return "Update recipe"

@recipeApi.route("<int:menuId>/delete/<int:id>/", methods=['DELETE'])
def recipeDelete(menuId, id):
    return "Delete recipe"