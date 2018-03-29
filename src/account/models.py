import uuid
from django.db import models
from django.contrib.auth.models import UserManager as DefaultUserManager, AbstractUser


class UserManager(DefaultUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        super().create_user(username=uuid.uuid4(), email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        super().create_superuser(username=uuid.uuid4(), email=email, password=password, **extra_fields)


class User(AbstractUser):
    """Model definition for User."""

    objects = UserManager()

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.',
        }
    )

    gender = models.ForeignKey(
        'Gender',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    gender = models.ForeignKey(
        'Gender',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Gender(models.Model):
    """Model definition for Gender."""

    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    REFERRED_AS_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
    )

    gender = models.CharField(
        max_length=255
    )
    referered_as = models.CharField(
        max_length=1,
        choices=REFERRED_AS_CHOICES,
        default=FEMALE,
    )

    class Meta:
        """Meta definition for Gender."""

        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        """Unicode representation of Gender."""
        return self.gender
