from django.http import JsonResponse


def getRoutes(request):
    routes = [
        '/token',
        '/token/refresh'
    ]
    return JsonResponse(routes, safe=False)
