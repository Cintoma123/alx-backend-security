# your_app/management/commands/block_ip.py

from django.core.management.base import BaseCommand
from ip_tracking.models import BlacklistedIP

class Command(BaseCommand):
    help = 'Block an IP by adding it to the blacklist'

    def add_arguments(self, parser):
        parser.add_argument('ip_address', type=str, help='IP address to block')
        parser.add_argument('--reason', type=str, default='', help='Reason for blocking')

    def handle(self, *args, **kwargs):
        ip = kwargs['ip_address']
        reason = kwargs['reason']

        if not BlacklistedIP.objects.filter(ip_address=ip).exists():
            BlacklistedIP.objects.create(ip_address=ip, reason=reason)
            self.stdout.write(self.style.SUCCESS(f"Successfully blocked IP: {ip}"))
        else:
            self.stdout.write(self.style.WARNING(f"IP {ip} is already blocked"))
