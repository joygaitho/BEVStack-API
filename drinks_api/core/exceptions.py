from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied, NotAuthenticated
from django.http import Http404


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response(
            {
                "error": "Internal server error"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if isinstance(exc, ValidationError):
        response.data = {
            "error": "Validation error",
            "details": response.data
        }

    elif isinstance(exc, NotAuthenticated):
        response.data = {
            "error": "Authentication credentials were not provided"
        }

    elif isinstance(exc, PermissionDenied):
        response.data = {
            "error": "You do not have permission to perform this action"
        }

    elif isinstance(exc, Http404):
        response.data = {
            "error": "ObjectDoesNotExist"
        }

    return response
