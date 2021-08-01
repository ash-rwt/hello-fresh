from flask import Blueprint

instructionApi = Blueprint('instructionApi', __name__)

@instructionApi.route("<int:recipeId>/list/", methods=['GET'])
def instructionList(recipeId):
    return "list of ingreadient by recipe"

@instructionApi.route("<int:recipeId>/list-by-id/<int:id>/", methods=['GET'])
def instructionListById(recipeId, id):
    return "list of instruction"

@instructionApi.route("<int:recipeId>/add/", methods=['POST'])
def instructionAdd(recipeId):
    return "Add instruction"

@instructionApi.route("<int:recipeId>/update/<int:id>/", methods=['PUT'])
def instructionUpdate(id):
    return "Update instruction"

@instructionApi.route("<int:recipeId>/delete/<int:id>/", methods=['DELETE'])
def instructionDelete(id):
    return "Delete instruction"