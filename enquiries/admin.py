from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'preferred_location', 'created_at')
    search_fields = ('name', 'email', 'message')
