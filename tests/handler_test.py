import unittest
import webapp2, webtest
from test_wsgi import app


class Web_Handler_Test(unittest.TestCase):
    def setUp(self):
        self.cookies = {}
        self.testapp = webtest.TestApp(app, cookiejar=self.cookies)

    def test_api_handler(self):
        resp = self.testapp.get('/api')
