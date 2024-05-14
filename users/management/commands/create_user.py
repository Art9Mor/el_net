from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Create a simple user'

    def handle(self, *args, **options):
        user = User.objects.create(
            email='simpleuser@elnet.com',
            first_name='John',
            last_name='Doe',
            role='user',
            is_active=True,
        )

        user.set_password('simpleuserpassword')
        user.save()
