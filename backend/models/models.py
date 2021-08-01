import datetime
from flask import request
from config.apps import db

class Menu(db.Model):
    __tablename__ = 'menu'
    menu_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    rating = db.Column(db.DECIMAL(asdecimal=False), default=0.0)
    img_url = db.Column(db.String(50), nullable=True)
    recipes = db.relationship('Recipe', backref='menu', lazy='dynamic')

    create_time = db.Column('created_at', db.DateTime, default=datetime.datetime.now)
    update_time = db.Column('last_updated', db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.menu_id)

class RecipeIngredient(db.Model):
   __tablename__ = 'recipe_ingredient'
   recipe_id = db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.recipe_id'), primary_key=True)
   ingredient_id = db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.ingredient_id'), primary_key=True)
   quantity = db.Column('quantity', db.DECIMAL(asdecimal=False)),


class Recipe(db.Model):
    __tablename__ = 'recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'))
    name = db.Column(db.String(20))
    description = db.Column(db.Text())
    img_url = db.Column(db.String(255))
    instructions = db.relationship('Instruction', backref='recipe', lazy='dynamic')
    ingredients = db.relationship('Ingredient', secondary='recipe_ingredient', lazy='subquery', backref=db.backref('recipe', lazy=True))
    
    create_time = db.Column('created_at', db.DateTime, default=datetime.datetime.now)
    update_time = db.Column('last_updated', db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.recipe_id)

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.Text())
    img_url = db.Column(db.String(255))
    measure_number = db.Column(db.Integer)
    measure_type = db.Column(db.String(20))
    energy = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    carbohydrate = db.Column(db.Integer)
    protien = db.Column(db.Integer)
    sodium = db.Column(db.Integer)
    recipes = db.relationship('Recipe', secondary='recipe_ingredient', lazy='subquery', backref=db.backref('ingredient', lazy=True))
    
    create_time = db.Column('created_at', db.DateTime, default=datetime.datetime.now)
    update_time = db.Column('last_updated', db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Instruction(db.Model):
    instruction_id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
    description = db.Column(db.Text())
    step_number = db.Integer
    img_url = db.Column(db.String(255))

    create_time = db.Column('created_at', db.DateTime, default=datetime.datetime.now)
    update_time = db.Column('last_updated', db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)