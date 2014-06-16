import webapp2, webtest
from handlers import ApiHandler
from wsgiref.simple_server import make_server
import datetime 

class Test_ApiHandler(ApiHandler):
    def get(self):
        return self.output({"test":123, "time":datetime.datetime(2014,6,10)})

    def post(self):
        raise Exception('error')

app = webapp2.WSGIApplication([
    webapp2.Route('/api', handler=Test_ApiHandler, name='test-apihandler'),
])


if __name__ == '__main__':
    httpd = make_server('', 8082, app)
    print "Serving on port 8000..."
    httpd.serve_forever()
