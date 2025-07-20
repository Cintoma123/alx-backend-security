
import logging
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime

logger = logging.getLogger(__name__)

BLACKLISTED_IPS = [
    '192.168.0.5',
    '203.0.113.10',
]

class IPLoggingMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.get_client_ip
        path = request.path
        user = request.user
        timestamp =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
           if request.user.is_authenticated:
              print("User is authenticated")
            else:
                print("Anonymous")
except AttributeError:
    print("Request object doesn't have a user")

    def get_client_ip(request):
         x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        try:
           if x_forwarded_for:
            ip =  x_forwarded_for.split(",")[0]
           else:
             ip = request.META.get("REMOTE_ADDR")
        return ip 

class BlockIPMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        ip = request.get_client_ip
        try:
            if ip in BLACKLISTED_IPS:
                return HttpResponseForbidden("Access denied. Your IP is blacklisted.")
            return get_response(request)

    def get_client_ip(request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        try:
            if x_forwarded_for:
                ip =  x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip 



