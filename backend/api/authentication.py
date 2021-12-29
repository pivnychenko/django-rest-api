from rest_framework import authentication
from rest_framework import exceptions
from apps.employee.models import Employee


class ExampleAuthentication(authentication.BaseAuthentication):

    def has_object_permission(self, request, *args, **kwargs):
        return getattr(request.user, 'phone_number', None)

    def has_permission(self, request, *args, **kwargs):
        return getattr(request.user, 'phone_number', None)

    def authenticate(self, request, *args, **kwargs):
        """
        Returns a `User` if a correct username and password have been supplied
        using HTTP Basic authentication.  Otherwise returns `None`.
        """
        phone_number = request.META.get('HTTP_X_USERNAME') # get the phone_number request header

        user = getattr(request._request, 'user', None)


        if not phone_number: # no phone_number passed in request headers
            return None

        try:
            user = Employee.objects.get(phone_number=phone_number) # get the user
        except Employee.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist

        return (user, None)