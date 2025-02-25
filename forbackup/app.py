from flask import Flask, send_from_directory, jsonify
from db import db
from routes import food_bp
import config
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:krish123@localhost/food_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Register the blueprint for routes (assuming food_bp is defined in routes.py)
app.register_blueprint(food_bp)

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the Food API!"

# Route for serving the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Route for '/egg' to get the nutritional information of an egg
@app.route('/egg', methods=['GET'])
def get_egg_info():
    egg = {
        'name': 'Egg',
        'protein': 6.3,
        'fat': 5.0,
        'carbs': 0.6
    }
    return egg



# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created in the database
    app.run(debug=True)
