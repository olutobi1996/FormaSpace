from django.contrib import admin
from .models import Enquiry
from .models import Subscriber


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company_name',
        'email',
        'phone',
        'team_size',
        'move_in_timeline',
        'budget_range',
        'created_at',
    )
    search_fields = ('name', 'email', 'company_name')
    list_filter = ('move_in_timeline', 'created_at')


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined')
