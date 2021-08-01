from schemas.InstructionSchema import *
from schemas.RecipeSchema import Recipe

from flask_restful import Resource

class InstructionListResource(Resource):
    def get(self, recipe_id):
        instructions = Instruction.query.filter_by(recipe_id=recipe_id).all()
        return instructions_schema.dump(instructions)

    def post(self, recipe_id):
        recipe = Recipe.query.get_or_404(request.json['recipe_id'])
        
        new_instruction = Instruction(
            recipe_id   = request.json['recipe_id'], 
            step_number = request.json['step_number'], 
            name        = request.json['name'],
            description = request.json['description'],
            img_url     = request.json['img_url'],
        )
        db.session.add(new_instruction)
        db.session.commit()
        return instruction_schema.dump(new_instruction)

class InstructionOneResource(Resource):
    def get(self, recipe_id, instruction_id):
        instruction = Instruction.query.get_or_404(instruction_id)
        return instruction_schema.dump(instruction)

    def patch(self, recipe_id, instruction_id):
        Recipe.query.get_or_404(request.json['recipe_id'])
        instruction = Instruction.query.get_or_404(instruction_id)

        for field in request.json:
           if field in request.json and field != "instruction_id":
                setattr(instruction, field, request.json[field])

        db.session.commit()
        return instruction_schema.dump(instruction)

    def delete(self, recipe_id, instruction_id):
        instruction = Instruction.query.get_or_404(instruction_id)
        db.session.delete(instruction)
        db.session.commit()
        return '', 204
