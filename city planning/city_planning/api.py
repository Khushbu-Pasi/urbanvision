from flask import Blueprint, request, jsonify
import asyncio

api = Blueprint('api', __name__)

@api.route('/get_address', methods=['POST'])
def get_address():
    # Import the function from the original app.py
    from city_planning.app import get_address
    return get_address()

@api.route('/analyze_area', methods=['POST'])
def analyze_area_endpoint():
    from city_planning.app import analyze_area
    data = request.json
    # Run the async function using asyncio
    return asyncio.run(analyze_area())

@api.route('/search_location', methods=['POST'])
def search_location():
    from city_planning.app import search_location
    return search_location()

@api.route('/detect_entities', methods=['POST'])
def detect_entities_endpoint():
    from city_planning.app import detect_entities
    return detect_entities()

# Function to register this blueprint with another Flask app
def register_api(app):
    app.register_blueprint(api, url_prefix='/city_planning') 