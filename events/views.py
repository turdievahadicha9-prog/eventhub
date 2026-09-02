
from rest_framework import viewsets
from .models import Category, Location, Event, Review
from .serializers import (
    CategorySerializer,
    LocationSerializer,
    EventSerializer,
    ReviewSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filterset_fields = ["category", "location"]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "date", "created_at"]
    ordering = ["date"]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer