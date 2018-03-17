import uuid
from django.db import models
from django.contrib.auth.models import UserManager as DefaultUserManager, AbstractUser

class UserManager(DefaultUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        super().create_user(username=uuid.uuid4(), email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        super().create_superuser(username=uuid.uuid4(), email=email, password=password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()

    email = models.EmailField(unique=True,
        error_messages={'unique': 'A user with that email already exists.'})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
