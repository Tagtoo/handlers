import unittest
import webapp2, webtest
from test_wsgi import app


class Web_Handler_Test(unittest.TestCase):
    def setUp(self):
        self.cookies = {}
        self.testapp = webtest.TestApp(app, cookiejar=self.cookies)

    def test_api_handler(self):
        resp = self.testapp.get('/api')
        self.assertEqual(resp.body, '{"test": 123, "time": "2014-06-10 00:00:00"}')

        resp = self.testapp.post('/api', status=500)
        self.assertEqual(resp.body, '{"error": {"message": "error", "code": "UnknowException", "type": "UnknowException"}}')
        raise Exception('test')
