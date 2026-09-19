from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    home,
    event_detail,
    category_events,
    location_events,
    CategoryViewSet,
    LocationViewSet,
    EventViewSet,
    ReviewViewSet,
)

# HTML барактар
urlpatterns = [
    path("", home, name="home"),
    path("event/<int:pk>/", event_detail, name="event-detail"),
    path("category/<int:pk>/", category_events, name="category-events"),
    path("location/<int:pk>/", location_events, name="location-events"),
]


# API
router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("locations", LocationViewSet)
router.register("events", EventViewSet)
router.register("reviews", ReviewViewSet)

urlpatterns += router.urls