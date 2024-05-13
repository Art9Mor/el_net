from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class UsersRole(models.TextChoices):
    """
    Roles for registered users.
    """
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractUser):
    """
    User model.
    """
    username = None

    email = models.EmailField(unique=True, verbose_name="Email Address")
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    role = models.CharField(max_length=50, choices=UsersRole.choices, verbose_name="Role")
    is_active = models.BooleanField(default=True, verbose_name="Activity")

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    @property
    def is_admin(self):
        return self.role == UsersRole.ADMIN

    @property
    def is_user(self):
        return self.role == UsersRole.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
