from functools import wraps

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings


def custom_view_decorator(view_function):
    @wraps(view_function)
    @api_view(['GET', 'POST'])
    def wrap(request, *args, **kwargs):
        auth = request.headers.get("Authorization", None)
        if not auth:
            return Response(dict(error='Authorization header required'), status=status.HTTP_401_UNAUTHORIZED)

        if auth != "Bearer "+settings.API_TOKEN:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        return view_function(request._request, *args, **kwargs)
    return wrap

