from django.contrib import admin

from .models import Category, Location, Event, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "location",
        "date",
        "price",
    )

    list_filter = (
        "category",
        "location",
    )

    search_fields = (
        "title",
        "description",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "event",
        "name",
        "rating",
    )