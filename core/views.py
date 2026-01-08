from django.http import JsonResponse

def health_check(request):
    """
    A simple health check endpoint.
    """
    return JsonResponse({"status": "ok"})
