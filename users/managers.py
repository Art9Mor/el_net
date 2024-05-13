from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password, role='user'):
        """
        Creates and saves a User with the given email, password, last and first names and role
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password, role='admin'):
        """
        Creates and saves a superuser with the given email, password, last and first names and role.
        """
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role,
        )

        user.is_active = True

