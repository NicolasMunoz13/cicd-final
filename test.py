import unittest
from calculator import app
with app.test_client() as c:
    response = c.get('/')
    print(response.data)
    assert response.data == b'Hello World. Welcome to the CI/CD app'
    assert response.status_code == 200