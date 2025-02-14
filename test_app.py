import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, Flask with Jenkins CD Pipeline!")

if __name__ == '__main__':
    unittest.main()
