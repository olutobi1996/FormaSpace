from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='locations/')
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

