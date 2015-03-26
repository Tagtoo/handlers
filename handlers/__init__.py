# TODO:
# 1. create a default Api Handler
# 2. handle json datatime
# 3. set response content_type "application/json"
# 4. extend json to support date / datatime (important)
# 5. handle callback automatically
# 6. write test case


from handlers import ApiHandler
from responses import JsonResponse, JsonpResponse
from errors import PermissionDeniedError, Error
