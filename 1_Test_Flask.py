import hello_world
import unittest
#https://circleci.com/blog/build-cicd-piplines-using-docker/

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_message(self):
        response = self.app.get('/')
        message = hello_world.wrap_html('Hello DockerCon 2018!')
        self.assertEqual(response.data, message)

if __name__ == '__main__':
    unittest.main()