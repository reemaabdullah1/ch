
from django.contrib.auth import authenticate, login
from django.utils.deprecation import MiddlewareMixin

class TokenAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header:
            try:
                auth_type, token = auth_header.split()
                if auth_type == 'Bearer':
                    user = authenticate(request=request, token=token)
                    if user is not None:
                        login(request, user)
            except:
                pass