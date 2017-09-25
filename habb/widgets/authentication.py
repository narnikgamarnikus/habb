from tastypie.authentication import Authentication

from tastypie.compat import (
    get_user_model, get_username_field, unsalt_token, is_authenticated
)
from tastypie.http import HttpUnauthorized


class CryptographicApiKeyAuthentication(Authentication):
    """
    Handles API key auth, in which a user provides a username & API key.
    Uses the ``ApiKey`` model that ships with tastypie. If you wish to use
    a different model, override the ``get_key`` method to perform the key check
    as suits your needs.
    """
    auth_type = 'cryptographicapikey'

    def _unauthorized(self):
        return HttpUnauthorized()

    def extract_credentials(self, request):
        try:
            data = self.get_authorization_data(request)
        except ValueError:
            username = request.GET.get('username') or request.POST.get('username')
            api_key = request.GET.get('api_key') or request.POST.get('api_key')
            token = request.GET.get('token') or request.POST.get('token')
        else:
            username, api_key, token = data.split(':', 1)

        return username, api_key, token

    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.
        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """
        try:
            username, api_key, token = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()

        if not username or not api_key or not token:
            return self._unauthorized()

        username_field = get_username_field()
        User = get_user_model()

        lookup_kwargs = {username_field: username}
        try:
            user = User.objects.select_related('api_key').get(**lookup_kwargs)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()

        if not self.check_active(user):
            return False

        key_auth_check = self.get_key(user, api_key, token)
        if key_auth_check and not isinstance(key_auth_check, HttpUnauthorized):
            request.user = user

        return key_auth_check

    def get_key(self, user, api_key, token):
        """
        Attempts to find the API key for the user. Uses ``ApiKey`` by default
        but can be overridden.
        """
        from tastypie.models import ApiKey

        from .utils import decode_token

        try:
            if user.api_key.key != api_key:
                return self._unauthorized()

            user_token = token#decode_token(token)

            if str(user.one_time_token) != user_token:
                return self._unauthorized()

        except ApiKey.DoesNotExist:
            return self._unauthorized()

        return True

    def get_identifier(self, request):
        """
        Provides a unique string identifier for the requestor.
        This implementation returns the user's username.
        """
        try:
            username = self.extract_credentials(request)[0]
        except ValueError:
            username = ''
        return username or 'nouser'