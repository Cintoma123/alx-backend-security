from django.db import models
class RequestLog  (models.Model):
# Create your models here.class IPLog(models.Model):
    ip_address = models.GenericIPAddressField()
    endpoint = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)


# models.py

class BlacklistedIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

