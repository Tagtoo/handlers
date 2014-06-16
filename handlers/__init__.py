# TODO:
# 1. create a default Api Handler
# 2. handle json datatime
# 3. set response content_type "application/json"
# 4. extend json to support date / datatime (important)
# 5. handle callback automatically
# 6. write test case

def extend_json(obj):
    if isinstance(obj, date):
        return str(obj)
    elif isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, Decimal):
        return float(obj)


class Error(Exception):
    pass

class PermissionDeniedError(Error):
    pass


class JsonResponse(webapp2.HttpResponse):
    def __init__(self, data, response):
        pass

class ApiHandler(webapp2.RequestHandler):
    def output(self, data):
        return JsonResponse()

    def format_exception(self, message, _type, code=None, status=400):
        code = code or _type

        self.response.set_status(status)
        self.JsonResponse({
            "error": {
                "message": message,
                "type": _type,
                "code": code
            }
        })

    def handle_exception(self, exception, debug):
        if isinstance(exception, AssertionError):
            self.format_exception(exception.message, "InvalidParameters")
        elif isinstance(exception, NotImplementedError):
            self.format_exception(exception.message, "InvalidOperation")
        elif isinstance(exception, PermissionDeniedError):
            self.format_exception(exception.message, "PermissionDenied")
        else:
            raise


class UserApi(ApiHandler):
    def get(self):
        self.output(data)
