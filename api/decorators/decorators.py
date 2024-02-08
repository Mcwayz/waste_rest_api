from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from base.models import User


def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == User.ADMIN:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return _wrapped_view


def customer_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == User.CUSTOMER:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return _wrapped_view


def collector_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role == User.COLLECTOR:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return _wrapped_view