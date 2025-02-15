import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client before running tests."""
        self.app = app.test_client()

    def test_home(self):
        """Test the home route '/'"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.data, b"Hello, Flask with Jenkins CD Pipeline!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
