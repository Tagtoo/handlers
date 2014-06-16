import webapp2
from .responses import JsonResponse, JsonpResponse
from .errors import PermissionDeniedError

class ApiHandler(webapp2.RequestHandler):
    def output(self, data):

        callback = self.request.get('callback', None)

        if callback:
            return JsonpResponse(callback=callback, data=data, response=self.response)
        else:
            return JsonResponse(data=data, response=self.response)

    def format_exception(self, message, _type, code=None, status=500):
        code = code or _type

        data = {
            "error": {
                "message": message,
                "type": _type,
                "code": code
            }
        }

        resp = self.output(data)
        resp.set_status(status)
        return resp

    def handle_exception(self, exception, debug):
        if isinstance(exception, AssertionError):
            return self.format_exception(exception.message, "InvalidParameters")
        elif isinstance(exception, NotImplementedError):
            return self.format_exception(exception.message, "InvalidOperation")
        elif isinstance(exception, PermissionDeniedError):
            return self.format_exception(exception.message, "PermissionDenied")
        else:
            return self.format_exception(exception.message, "UnknowException")




