from django.contrib import admin
from .models import Enquiry
from .models import Subscriber

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'preferred_location', 'created_at')
    search_fields = ('name', 'email', 'message')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined')
