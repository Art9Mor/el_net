from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Creates admin users'

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.ad',
            first_name='Admin',
            last_name='User',
            role='admin',
            is_active=True
        )

        user.set_password('666')
        user.save()
