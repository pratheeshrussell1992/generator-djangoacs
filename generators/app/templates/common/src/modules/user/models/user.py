from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _ 
from django.conf import settings 
from datetime import date 

# https://www.geeksforgeeks.org/creating-custom-user-model-using-abstractuser-in-django_restframework/
# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
# https://hashedin.com/blog/configure-role-based-access-control-in-django/
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser): 
  username = None # should be set explicitly since username is a mandatory field
  first_name = models.CharField(max_length = 100, blank = False, null = True) 
  last_name = models.CharField(max_length = 100, blank = False, null = True)
  email = models.EmailField(unique = True) 
  password = models.CharField(max_length = 500, blank = False, null = True)
  phone_no = models.CharField(max_length = 10) 
  gender= models.CharField(max_length = 100, blank = False, null = True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']
  objects = UserManager()

