from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r"users", UserViewSet, basename="users")
# router.register(r"my", MyPageViewSet, basename="my")

urlpatterns = [
    path("", include(router.urls)),
]