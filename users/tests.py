from rest_framework.test import APITestCase

from users.models import User
from users.serializers import CustomUserCreateSerializer


class UsersTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create(
            email='gork@mork.ork',
            first_name='Gork',
            last_name='Mork',
            password='1234qwer5678',
            role='user'
        )

        self.client.force_authenticate(user=self.user)

    def test_user_creation(self):
        data = {
            'email': 'test1@example.com',
            'first_name': 'Test1',
            'last_name': 'User1',
            'password': 'testpassword',
            'password2': 'testpassword',
            'role': 'user'
        }

        self.serializer = CustomUserCreateSerializer(data=data)
        self.assertTrue(self.serializer.is_valid(), msg=self.serializer.errors)
        user_instance = self.serializer.save()

        self.assertEqual(user_instance.email, data['email'])
        self.assertEqual(user_instance.first_name, data['first_name'])
        self.assertEqual(user_instance.last_name, data['last_name'])
        self.assertEqual(user_instance.role, data['role'])

