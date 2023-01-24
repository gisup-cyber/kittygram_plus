from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 