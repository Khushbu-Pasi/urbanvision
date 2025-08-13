# Linking the City Planning Project to Other Projects

This document outlines different methods to incorporate the City Planning functionality into other projects.

## Method 1: Install as a Package

This project can be installed as a Python package in another project.

```bash
# Option 1: Install directly from the directory
pip install -e /path/to/city_planning

# Option 2: Install from GitHub repository
pip install git+https://github.com/username/city_planning.git
```

Then in your project:

```python
# Import and use the Flask app directly
from city_planning import app as city_planning_app

# OR use the API blueprint
from city_planning.api import register_api

# Register the city planning API with your existing Flask app
from flask import Flask
app = Flask(__name__)
register_api(app)
```

## Method 2: Use as a Git Submodule

Add this project as a submodule to your existing project:

```bash
cd your_project
git submodule add https://github.com/username/city_planning.git
git submodule update --init --recursive
```

## Method 3: REST API Integration

If the city planning project is running as a separate service, you can integrate with it via REST API calls:

```python
import requests

# Make API calls to the city planning service
response = requests.post('http://city-planning-service/analyze_area', json={'bounds': {...}})
results = response.json()
```

## Method 4: Docker Compose Integration

Create a docker-compose.yml file that includes both services:

```yaml
version: '3'
services:
  your-app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - city-planning

  city-planning:
    build: ./city_planning
    ports:
      - "5000:5000"
```

## Method 5: Use as a Frontend Component

If you need just the frontend components:

1. Copy the relevant templates from the `templates` directory
2. Copy the required static assets from the `static` directory
3. Implement the necessary API endpoints in your application

## Method 6: Shared Database

If both projects need to share data:

1. Configure both applications to use the same database
2. Ensure consistent database schema and models
3. Use database transactions to maintain data integrity 