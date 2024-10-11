from django.http import HttpResponseForbidden


# class IPRestrictMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request, *args, **kwargs):
#         client_ip = request.META.get('REMOTE_ADDR')
#
#         ip_address = (
#             '172.18.0.1',
#             '255.0.0.0',
#             '255.255.255.0',
#             '10.10.3.146',
#             '192.168.145.106',
#             '10.10.3.180',
#             '192.168.100.41',
#         )
#         if client_ip not in ip_address and request.path.find('/admin/') != -1:
#             return HttpResponseForbidden('Permission denied')
#         response = self.get_response(request)
#         return response

from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
import logging


class IPRestrictMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = getattr(settings, 'ALLOWED_ADMIN_IPS', [])
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        self.logger.debug(f"Client IP: {client_ip}")

        if request.path.startswith('/admin/') and client_ip not in self.allowed_ips:
            self.logger.warning(f"Forbidden access attempt by IP: {client_ip}")
            return HttpResponseForbidden('Permission denied')

        response = self.get_response(request)
        return response
