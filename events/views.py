from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Category, Location, Event, Review
from .serializers import (
    CategorySerializer,
    LocationSerializer,
    EventSerializer,
    ReviewSerializer,
)


def home(request):
    query = request.GET.get("q", "").strip()

    events = Event.objects.select_related("category", "location").all()

    if query:
        events = events.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(category__name__icontains=query)
            | Q(location__name__icontains=query)
        )

    categories = Category.objects.all()
    locations = Location.objects.all()

    return render(request, "events/home.html", {
        "events": events,
        "categories": categories,
        "locations": locations,
        "query": query,
    })


def event_detail(request, pk):
    event = get_object_or_404(
        Event.objects.select_related("category", "location"),
        pk=pk
    )
    reviews = event.reviews.all()

    return render(request, "events/event_detail.html", {
        "event": event,
        "reviews": reviews,
    })


def category_events(request, pk):
    category = get_object_or_404(Category, pk=pk)

    events = Event.objects.filter(
        category=category
    ).select_related("category", "location")

    return render(request, "events/category_events.html", {
        "category": category,
        "events": events,
    })


def location_events(request, pk):
    location = get_object_or_404(Location, pk=pk)

    events = Event.objects.filter(
        location=location
    ).select_related("category", "location")

    return render(request, "events/location_events.html", {
        "location": location,
        "events": events,
    })


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related(
        "category", "location"
    ).all()

    serializer_class = EventSerializer

    filter_backends = [SearchFilter]
    search_fields = [
        "title",
        "description",
        "category__name",
        "location__name",
    ]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer