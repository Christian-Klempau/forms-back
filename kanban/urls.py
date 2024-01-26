from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"board", views.BoardViewSet, basename="board")
router.register(r"card", views.CardViewSet, basename="card")
router.register(r"category", views.CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
