import unittest
from calculator import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World. This is a calculator! <br/> The sum operation with 3 and 2 is 5<br/>The substract operation with 3 and 2 is 1'
    assert response.status_code == 200