from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from overpy import Overpass
import json
from folium import Map, Marker, Icon, FeatureGroup
import folium
import pandas as pd
import numpy as np
from scipy.spatial import distance
from collections import Counter
from sklearn.cluster import DBSCAN
from shapely.geometry import Point, Polygon
import geopandas as gpd
import spacy
from folium import plugins
from folium.plugins import Draw, MousePosition, MeasureControl
import branca.colormap as cm
import asyncio
import torch

# Load environment variables
load_dotenv()

app = Flask(__name__, 
            static_folder='../static',
            template_folder='../templates')
CORS(app)

# Initialize models - Replace with alternative NER implementation
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import subprocess
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Initialize geocoder and Overpass API
geolocator = Nominatim(user_agent="urban_development_planner")
overpass_api = Overpass()

# Import all the routes and functions from the original app.py
# ... existing code ...

def create_app(config=None):
    """Factory function to create the Flask application"""
    if config:
        app.config.update(config)
    return app
    
if __name__ == '__main__':
    app.run(debug=True) 