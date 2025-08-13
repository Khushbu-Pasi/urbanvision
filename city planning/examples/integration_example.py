"""
Example of integrating the city planning project into another Flask application
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
from city_planning.api import register_api
from city_planning import app as city_planning_app

# Create a new Flask app
app = Flask(__name__)

# Option 1: Register the city planning API as a blueprint
register_api(app)

# Option 2: Import specific functionality
from city_planning.app import analyze_map_entities, generate_recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Use imported functions from city planning project
    data = request.json
    entities = data.get('entities', [])
    
    # Use city planning functionality
    analysis = analyze_map_entities(entities)
    recommendations = generate_recommendations(analysis)
    
    return jsonify({
        'analysis': analysis,
        'recommendations': recommendations
    })

@app.route('/city_planning_redirect')
def redirect_to_city_planning():
    # Redirect to the city planning UI
    return redirect(url_for('city_planning.index'))

if __name__ == '__main__':
    app.run(debug=True, port=8000) 