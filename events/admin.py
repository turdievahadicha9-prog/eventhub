from django.contrib import admin
from .models import Category, Location, Event, Review


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Review)