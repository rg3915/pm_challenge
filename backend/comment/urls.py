from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, TagViewSet

router = routers.DefaultRouter()

router.register(r'tags', TagViewSet)

router.register(r'comments', CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
