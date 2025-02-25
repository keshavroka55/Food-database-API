from flask import Blueprint, request, jsonify
from models import Food, db

food_bp = Blueprint('food_bp', __name__)

# 🟢 1️⃣ GET - Retrieve food by name
@food_bp.route('/food/<name>', methods=['GET'])
def get_food(name):
    food = Food.query.filter_by(name=name).first()
    if food:
        return jsonify({"name": food.name, "protein": food.protein, "fat": food.fat, "carbs": food.carbs})
    return jsonify({"error": "Food not found"}), 404

# 🟡 2️⃣ POST - Add a new food item
@food_bp.route('/food', methods=['POST'])
def add_food():
    data = request.json
    new_food = Food(name=data['name'], protein=data['protein'], fat=data['fat'], carbs=data['carbs'])
    db.session.add(new_food)
    db.session.commit()
    return jsonify({"message": "Food added"}), 201

#  PUT - Update food details
@food_bp.route('/food/<name>', methods=['PUT'])
def update_food(name):
    food = Food.query.filter_by(name=name).first()
    if food:
        data = request.json
        food.protein = data.get('protein', food.protein)
        food.fat = data.get('fat', food.fat)
        food.carbs = data.get('carbs', food.carbs)
        db.session.commit()
        return jsonify({"message": "Food updated"})
    return jsonify({"error": "Food not found"}), 404

# 🔴 4️⃣ DELETE - Remove a food item
@food_bp.route('/food/<name>', methods=['DELETE'])
def delete_food(name):
    food = Food.query.filter_by(name=name).first()
    if food:
        db.session.delete(food)
        db.session.commit()
        return jsonify({"message": "Food deleted"})
    return jsonify({"error": "Food not found"}), 404


