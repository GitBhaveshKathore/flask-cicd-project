import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data

def test_health():
    client = app.test_client()
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_info():
    client = app.test_client()
    response = client.get('/api/info')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['app'] == 'Flask CI/CD Demo'

def test_echo():
    client = app.test_client()
    response = client.get('/api/echo/hello')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['echo'] == 'hello'

def test_pipeline():
    client = app.test_client()
    response = client.get('/api/pipeline')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['pipeline'] == 'Jenkins CI/CD'
