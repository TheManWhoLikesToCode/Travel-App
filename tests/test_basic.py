import unittest, sys

sys.path.append('../../Travel-App') # imports python file from parent directory
from app import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_todo(self):
        response = self.app.get('/todo', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_destination(self):
        response = self.app.get('/destinations', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_about_us(self):
        response = self.app.get('/about_us', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()