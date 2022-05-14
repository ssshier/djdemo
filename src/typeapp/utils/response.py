from django.http import JsonResponse


def response_decorator(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        result = {
            "code": 200,
            "data": data,
            "message": "success"
        }
        return JsonResponse(data=result, json_dumps_params={'ensure_ascii': False})
    return wrapper