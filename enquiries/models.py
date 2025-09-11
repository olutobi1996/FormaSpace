from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    team_size = models.CharField(max_length=50, blank=True)
    move_in_timeline = models.CharField(
        max_length=50,
        blank=True,
        choices=[
            ("immediate", "Immediate"),
            ("1-3 months", "1–3 months"),
            ("6+ months", "6+ months"),
        ],
    )
    budget_range = models.CharField(max_length=100, blank=True)
    space_requirements = models.TextField(blank=True)
    message = models.TextField(blank=True)
    hear_about_us = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name} - {self.email}"




class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
