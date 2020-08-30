from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostReadOnlyViewSet

app_name = 'carts'

router = SimpleRouter()
router.register('', PostReadOnlyViewSet, basename='items')

urlpatterns = [
] + router.urls
