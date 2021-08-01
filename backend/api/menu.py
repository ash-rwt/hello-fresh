from flask import Blueprint
menuApi = Blueprint('menuApi', __name__)

@menuApi.route("/list/", methods=['GET'])
def menuList():
    return "list of Menu"

@menuApi.route("/list-by-id/<int:id>/", methods=['GET'])
def menuListById(id):
    return "list of Menu " + str(id)

@menuApi.route("/add/", methods=['GET'])
def menuAdd():
    dish = models.Menu(name='Lamb Kabab', description="This is awesome lamp kabab disk", rating=4.3)
    db.session.add(dish)
    db.session.commit()
    return "Add Menu"

@menuApi.route("/update/<int:id>/", methods=['PUT'])
def menuUpdate(id):
    return "Update Menu"

@menuApi.route("/delete/<int:id>/", methods=['DELETE'])
def menuDelete(id):
    return "Delete Menu"