from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {
    'null': True,
    'blank': True,
}


class Supplier(models.Model):
    """
    Supplier model
    """

    LEVEL_CHOICES = (
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Individual Entrepreneur'),
    )

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Owner', **NULLABLE)
    parent_supplier = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name='Parent supplier', **NULLABLE)

    title = models.CharField(max_length=255, verbose_name='Name of supplier')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Country')
    city = models.CharField(max_length=100, verbose_name='City')
    street = models.CharField(max_length=200, verbose_name='Street')
    hose_number = models.CharField(max_length=100, verbose_name='Hose Number')
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, verbose_name='Level')

    debt = models.DecimalField(max_digits=20, decimal_places=2, default=0, verbose_name='Department', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')

    def __str__(self):
        return f'{self.title}({self.level})'

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


class Product(models.Model):
    """
    Product model
    """

    owner = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Product owner', **NULLABLE)
    title = models.CharField(max_length=255, verbose_name='Title')
    model = models.CharField(max_length=255, verbose_name='Model')
    release_date = models.DateField(auto_now_add=True, verbose_name='Product release date', **NULLABLE)

    def __str__(self):
        return f'{self.model}: {self.title}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
