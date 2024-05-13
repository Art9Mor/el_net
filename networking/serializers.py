from rest_framework import serializers

from networking.models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model
    """

    salesman = serializers.CharField(source='owner.title', read_only=True)

    class Meta:
        model = Product
        fields = ('title', 'model', 'release_date', 'salesman')


class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer for Supplier model.
    """

    company_slug_name = serializers.SlugRelatedField(slug_field='title', queryset=Supplier.objects.all())
    owner_first_name = serializers.ReadOnlyField(source='owner.first_name', read_only=True)
    owner_last_name = serializers.ReadOnlyField(source='owner.last_name', read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)
        instance.__dict__.update(validated_data)
        instance.save()
        return instance

    class Meta:
        model = Supplier
        fields = '__all__'
