from django.urls import path, include
from rest_framework import routers

from networking import views
from networking.apps import NetworkingConfig

app_name = NetworkingConfig.name

router = routers.DefaultRouter()

router.register(r'api/products', views.ProductViewSet, basename='product')
router.register(r'api/suppliers', views.SupplierViewSet, basename='supplier')

urlpatterns = [
    path('', include(router.urls)),
]