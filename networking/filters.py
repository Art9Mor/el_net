import django_filters
from django_filters import FilterSet

from networking.models import Supplier


class SupplierFilter(FilterSet):
    """
    Supplier filter by city.
    """

    city = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Supplier
        fields = ['city']
