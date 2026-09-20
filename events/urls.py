from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
    home,
    event_detail,
    CategoryViewSet,
    LocationViewSet,
    EventViewSet,
    ReviewViewSet,
)


router = DefaultRouter()

router.register(
    "categories",
    CategoryViewSet,
    basename="category",
)

router.register(
    "locations",
    LocationViewSet,
    basename="location",
)

router.register(
    "events",
    EventViewSet,
    basename="event",
)

router.register(
    "reviews",
    ReviewViewSet,
    basename="review",
)


urlpatterns = [

    path(
        "event/<int:event_id>/",
        event_detail,
        name="event-detail",
    ),

]


urlpatterns += router.urls