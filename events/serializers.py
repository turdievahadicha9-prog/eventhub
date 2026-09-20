from rest_framework import serializers

from .models import Category, Location, Event, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    location_name = serializers.CharField(
        source="location.name",
        read_only=True
    )

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "category",
            "category_name",
            "location",
            "location_name",
            "date",
            "price",
            "image",
            "created_at",
        ]