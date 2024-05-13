from django.contrib import admin

from networking.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Displaying the Supplier model in the admin panel
    """
    list_display = ('id', 'title', 'owner_email', 'level', 'country', 'city', 'debt', 'created_at')
    list_filter = ('level', 'title', 'country', 'city')
    search_fields = ('level', 'country', 'city', 'owner_email')

    def owner_email(self, obj):
        return obj.owner.email

    def dept_reset(self, request, queryset):
        """
        Removes debts
        """
        for supplier in queryset:
            supplier.dept = 0
            supplier.save()
        self.message_user(request, 'Successfully removed all debts')

    owner_email.admin_order_field = 'owner_email'
    owner_email.short_description = 'Owner Email'
    dept_reset.short_description = 'Debt clearance'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Displaying the Product model in the admin panel
    """
    list_display = ('owner_title', 'title', 'model', 'release_date')
    list_filter = ('owner', 'title', 'model')
    search_fields = ('title',)

    def owner_title(self, obj):
        return obj.owner.title
