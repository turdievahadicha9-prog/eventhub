from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, serializers

from .models import (
    Category,
    Location,
    Event,
    Review,
)


# =====================================================
# SERIALIZERS
# =====================================================

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


# =====================================================
# API VIEWSETS
# =====================================================

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer


class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()

    serializer_class = LocationSerializer


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.select_related(
        "category",
        "location",
    ).all()

    serializer_class = EventSerializer

    search_fields = [
        "title",
        "description",
        "category__name",
        "location__name",
    ]

    ordering_fields = [
        "date",
        "price",
        "created_at",
    ]

    ordering = [
        "-date",
    ]


class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer


# =====================================================
# HOME PAGE
# =====================================================

def home(request):

    query = request.GET.get("q", "").strip()

    categories = Category.objects.all()

    events = Event.objects.select_related(
        "category",
        "location",
    ).all().order_by("date")

    if query:

        events = events.filter(
            title__icontains=query
        ) | events.filter(
            description__icontains=query
        ) | events.filter(
            category__name__icontains=query
        ) | events.filter(
            location__name__icontains=query
        )

        events = events.distinct()

    context = {
        "events": events,
        "categories": categories,
        "query": query,
    }

    return render(
        request,
        "events/home.html",
        context,
    )


# =====================================================
# EVENT DETAIL
# =====================================================

def event_detail(request, event_id):

    event = get_object_or_404(
        Event.objects.select_related(
            "category",
            "location",
        ),
        id=event_id,
    )

    reviews = Review.objects.filter(
        event=event
    ).order_by("-id")

    context = {
        "event": event,
        "reviews": reviews,
    }

    return render(
        request,
        "events/event_detail.html",
        context,
    )