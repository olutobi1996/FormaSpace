from django.db import models

class SocialIntegration(models.Model):
    platform = models.CharField(max_length=50)
    api_key = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.platform

