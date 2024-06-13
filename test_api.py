import unittest
from app import app, db, Data

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all() 

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_data(self):
        response = self.app.post('/data', json={"key": "value"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_data(self):
        data = Data(json_data={"key": "value"})
        db.session.add(data)
        db.session.commit()
        response = self.app.get(f'/data/{data.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"key": "value"})

    def test_update_data(self):
        data = Data(json_data={"key": "value"})
        db.session.add(data)
        db.session.commit()
        response = self.app.put(f'/data/{data.id}', json={"new_key": "new_value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], "Data updated")

    def test_delete_data(self):
        data = Data(json_data={"key": "value"})
        db.session.add(data)
        db.session.commit()
        response = self.app.delete(f'/data/{data.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], "Data deleted")

if __name__ == '__main__':
    unittest.main()
