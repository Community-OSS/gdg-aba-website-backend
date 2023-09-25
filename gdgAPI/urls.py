from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunityTalentViewSet

router = DefaultRouter()

router.register(r"community-talent", CommunityTalentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
