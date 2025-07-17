from django.contrib import admin
from .models import Restaurant, Review

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'author', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('author', 'comment')
