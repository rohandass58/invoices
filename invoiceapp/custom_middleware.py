from django.utils.deprecation import MiddlewareMixin


class AllowAllOriginsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
        return response
