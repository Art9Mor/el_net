from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'role')
    list_filter = ('is_active', 'role')