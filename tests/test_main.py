import unittest

from fastapi_sqlalchemy import db
from main import app

from starlette.testclient import TestClient

from models import User


client = TestClient(app)



def test_load():
    response = client.get("/users/")
    print("Response:", response.json())
    assert response.status_code == 200


# class MainTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         self.client = TestClient(app)

#         self.test_user = User(
#             first_name="Test User",
#             last_name="Testson",
#             age=44
#         )

#         # db.session.add(test_user)
#         # db.session.commit()
#         my_session.session.add(self.test_user)
#         my_session.session.commit()

#     def tearDown(self) -> None:
#         my_session.session.delete(self.test_user)
#         my_session.session.commit()
#         return super().tearDown()

#     def test_load_users(self):
#         output = self.client.get("/users/")
#         self.assertEqual(len(output.json()), 1)