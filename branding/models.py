from django.db import models

class BrandNameProposal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    domain_available = models.BooleanField(default=False)
    trademark_suitable = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
