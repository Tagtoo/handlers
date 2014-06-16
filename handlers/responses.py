import webapp2
import json


class TagtooJsonEncoder(json.JSONEncoder):
    def default(self, obj, **kwargs):
        import pdb;pdb.set_trace()
        print 'TagtooJsonEncoder'
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)



def JsonResponse(data, cls=TagtooJsonEncoder, response=None):
    response = response or webapp2.Response()
    response.write(json.dumps(data))
    response.content_type = 'application/javascript'
    
    return response
    

def JsonpResponse(callback, data, cls=TagtooJsonEncoder, response=None):
    response = response or webapp2.Response()
    data = json.dumps(data)
    body = '''{}({})'''.format(callback, data)
    response.write(body)
    response.content_type = 'text/html'
    
    return response
