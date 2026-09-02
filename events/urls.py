from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    LocationViewSet,
    EventViewSet,
    ReviewViewSet,
)

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("locations", LocationViewSet)
router.register("events", EventViewSet)
router.register("reviews", ReviewViewSet)

urlpatterns = router.urls