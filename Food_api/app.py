from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:krish123@localhost/food_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Food item model (Map to `food_items` table)
class FoodItem(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    protein = db.Column(db.Float)
    fat = db.Column(db.Float)
    carbs = db.Column(db.Float)

@app.route('/')
def home():
    return "Welcome to the Food API!"

@app.route('/egg', methods=['GET'])
def get_egg_info():
    # Fetch egg data from MySQL database
    egg = FoodItem.query.filter_by(name="Egg").first()
    if egg:
        return jsonify({
            'name': egg.name,
            'protein': egg.protein,
            'fat': egg.fat,
            'carbs': egg.carbs
        })
    return jsonify({"message": "Egg not found!"}), 404

@app.route('/rice', methods=['GET'])
def get_rice_info():
    # Fetch rice data from MySQL database
    rice = FoodItem.query.filter_by(name="Rice").first()
    if rice:
        return jsonify({
            'name': rice.name,
            'protein': rice.protein,
            'fat': rice.fat,
            'carbs': rice.carbs
        })
    return jsonify({"message": "Rice not found!"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created when the app starts

    # Use Waitress to serve the app instead of app.run()
    serve(app, host='0.0.0.0', port=5000)
