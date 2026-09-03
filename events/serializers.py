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


class EventSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "category",
            "location",
            "date",
            "price",
            "image",
            "created_at",
            "average_rating",
            "reviews_count",
        ]
        read_only_fields = ["average_rating", "reviews_count"]

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()

        if not reviews.exists():
            return 0

        total = sum(review.rating for review in reviews)
        return round(total / reviews.count(), 1)

    def get_reviews_count(self, obj):
        return obj.reviews.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"