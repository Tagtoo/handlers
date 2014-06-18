import webapp2
import json
import datetime
from decimal import Decimal


def TagtooJson(obj, *args):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, Decimal):
        return float(obj)





def JsonResponse(data, encoder=TagtooJson, response=None):
    response = response or webapp2.Response()
    response.write(json.dumps(data, default=encoder))
    response.content_type = 'application/javascript'

    return response


def JsonpResponse(callback, data, encoder=TagtooJson, response=None):
    response = response or webapp2.Response()
    data = json.dumps(data)
    body = '''{}({})'''.format(callback, data)
    response.write(body)
    response.content_type = 'text/html'

    return response
