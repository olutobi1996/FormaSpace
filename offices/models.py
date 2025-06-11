from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField(blank=True)
    parking_available = models.BooleanField(default=False)
    wifi_speed = models.CharField(max_length=50, blank=True)
    secure_access = models.BooleanField(default=True)
    kitchenette = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Office(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    office_number = models.CharField(max_length=10)
    specs = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.location.name} - Office {self.office_number}"

