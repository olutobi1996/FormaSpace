from django.contrib import admin
from .models import Post, Category, Event

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('published_at', 'categories')
    search_fields = ('title', 'content', 'tags')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date')
    list_filter = ('event_date',)

