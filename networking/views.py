from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from networking.filters import SupplierFilter
from networking.models import Product, Supplier
from networking.permissions import IsOwner, IsAdmin
from networking.serializers import ProductSerializer, SupplierSerializer
from users.models import User
from users.permissions import IsActiveEmployee


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsActiveEmployee, IsOwner | IsAdmin]
        else:
            permission_classes = [IsAuthenticated, IsActiveEmployee]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        supplier = self.request.user.supplier
        product = serializer.save(owner=supplier)
        product.save()


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsActiveEmployee, IsOwner | IsAdmin]
        else:
            permission_classes = [IsAuthenticated, IsActiveEmployee]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        user = self.request.user
        supplier = serializer.save(owner=user)
        supplier.save()
