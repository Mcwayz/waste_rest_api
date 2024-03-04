from django.http import HttpResponseForbidden
from django.shortcuts import render
from functools import wraps

def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_superuser:
            # Render forbidden page template
            return render(request, 'frontend/base/forbidden.html', status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view