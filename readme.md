1. Backend RESTFUL api project with Python flask framework and SQLAlchemy as ORM
2. Database used is postgres 
3. Dependencies description are stored in backend/requirements.txt
4. PORT opened for this api project: 7201, PORT opened for postgres database: 7200
5. API endpoints are - 
	MENU
		1. GET /api/menus - to list menus
		2. POST /api/menus - to add new menus
		3. GET /api/menu/<menu_id> - to view menu by id
		4. PATCH /api/menu/<menu_id> - to update menu by id
		5. DELETE /api/menu/<menu_id> - to delete menu by id
	
	RECIPIES
		1. GET /api/<menu_id>/recipies - to list all recipies under menu <menu_id>
		2. POST /api/<menu_id>/recipies/ - to add new recipies under menu <menu_id>
		3. GET /api/<menu_id>/recipe/<recipy_id> - to view specific recipe by id, validated by <menu_id>
		4. PATCH /api/<menu_id>/recipe/<recipy_id> - to update recipe by id
		5. DELETE /api/<menu_id>/recipe/<recipy_id> - to delete recipe by id

	INGREDIENTS
		1. GET /api/ingredients - to list ingredients
		2. POST /api/ingredients - to add new ingredient
		3. GET /api/ingredients/<ingredient_id_id> - to view ingredient by id
		4. PATCH /api/ingredients/<ingredient_id_id> - to update ingredient by id
		5. DELETE /api/ingredients/<ingredient_id_id> - to delete ingredient by id
		
	INSTRUCTIONS
		1. GET /api/<recipe_id>/instructions - to list all instructions for specific recipe <recipe_id>
		2. POST /api/<recipe_id>/instructions/ - to add new instruction for specific recipe <recipe_id>
		3. GET /api/<recipe_id>/instruction/<recipe_id> - to view specific instruction step by id, validated by <recipe_id>
		4. PATCH /api/<recipe_id>/instruction/<recipe_id> - to update instruction by id
		5. DELETE /api/<recipe_id>/instruction/<recipe_id> - to delete instruction by id

6. Data Models file are stored in /models/model.py
7. Model Scheam are stored in /schemas directory
8. API Resources are stored in /resources/ directory
9. Config files are located in /config
10. DB migrations are stored in /migrations
11. .env stores the enviroment variables form app

TO DO more -
12. Token based Authentication
13. Add testing