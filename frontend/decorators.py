from django.contrib.auth import authenticate
from django.http import HttpResponseForbidden

def token_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Get the token from the request headers, cookies, or query parameters
        token = request.headers.get('Authorization')  # Example: Bearer <token>
        # Or: token = request.COOKIES.get('token')
        # Or: token = request.GET.get('token')

        # Perform token validation
        user = authenticate(request, token=token)
        if not user:
            return HttpResponseForbidden('Invalid token')

        # Token is valid, proceed to the view function
        return view_func(request, *args, **kwargs)

    return wrapper