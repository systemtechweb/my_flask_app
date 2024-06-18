import app
import os

def test_home_page():
    flask_app = app.create_app('config.py')
    print(flask_app)
    with flask_app.test_client() as test_client:
       response = test_client.get('/')
       assert response.status_code == 200
       assert b"Welcome to the" in response.data
