from django.http import JsonResponse

def health_check(request):
    """
    A simple health check endpoint.
    """
    return JsonResponse({"status": "ok"})

def home(request):
    """
    A simple home page endpoint.
    """
    return JsonResponse({"status": "ok", "message": "Welcome to the Sales CRM!"})
