handlers
========

the common handler interface

sample code
```python

from handlers import ApiHandler
from wsgiref.simple_server import make_server
import datetime 

class Test_ApiHandler(ApiHandler):
    def get(self):
        self.output({"test":123, "time":datetime.datetime(2014,6,10)})

    def post(self):
        raise Exception('error')

app = webapp2.WSGIApplication([
    webapp2.Route('/api', handler=Test_ApiHandler, name='test-apihandler'),
])
```
