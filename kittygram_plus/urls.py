from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    
] 