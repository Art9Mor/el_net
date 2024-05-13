from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from users.serializers import CustomUserCreateSerializer


class UsersTestCase(APITestCase):
    """
    Class for testing the user endpoints.
    """

    def setUp(self):
        """
        Preparing a test environment
        """

        self.user = User.objects.create(
            email='gork@mork.ork',
            first_name='Gork',
            last_name='Mork',
            password='1234qwer5678',
            role='user'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """
        Test user creation
        """
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

    def test_view_user_detail(self):
        """
        Test view user detail
        """

        response = self.client.get(
            f'/api/users/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_create_superuser(self):
        """
        Test superuser creation
        """

        self.hastur = User.objects.create(
            email='hastur@love.craft',
            first_name='Hastur',
            last_name='Lovecraft',
            password='golgofa666',
            role='admin'
        )

        print('Info:', self.hastur)
        self.assertEqual(self.hastur.is_admin, True)
