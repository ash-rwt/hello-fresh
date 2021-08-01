from schemas.MenuSchema import *
from flask_restful import Resource

class MenuListResource(Resource):
    def get(self):
        menus = Menu.query.all()
        return menus_schema.dump(menus)

    def post(self):
        new_menu = Menu(
            name = request.json['name'],
            description = request.json['description'],
            rating = request.json['rating'],
            img_url = request.json['img_url'],
        )
        db.session.add(new_menu)
        db.session.commit()
        return menu_schema.dump(new_menu)

class MenuOneResource(Resource):
    def get(self, menu_id):
        menu = Menu.query.get_or_404(menu_id)
        return menu_schema.dump(menu)

    def patch(self, menu_id):
        menu = Menu.query.get_or_404(menu_id)
        for field in request.json:
            if field in request.json and field != "menu_id":
                setattr(menu, field, request.json[field])

        db.session.commit()
        return menu_schema.dump(menu)

    def delete(self, menu_id):
        menu = Menu.query.get_or_404(menu_id)
        db.session.delete(menu)
        db.session.commit()
        return '', 204
