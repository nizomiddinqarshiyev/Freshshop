from django.http import HttpResponseForbidden


class IPRestrictMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        client_ip = request.META.get('REMOTE_ADDR')

        ip_address = (
            '172.18.0.1',
            '255.0.0.0',
            '255.255.255.0',
            '10.10.3.146',
            '192.168.145.106',
            '10.10.3.180'
        )
        if client_ip not in ip_address and request.path.find('/admin/') != -1:
            return HttpResponseForbidden('Permission denied')
        response = self.get_response(request)
        return response

