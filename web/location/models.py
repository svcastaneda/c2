from django.db import models

from address.models import AddressField


class Location(models.Model):
    """Model definition for Location."""

    SCHOOL = 'S'
    CLASS = 'C'
    HOME = 'H'
    WORK = 'W'
    LOCATION_TYPE_CHOICES = (
        (SCHOOL, 'School'),
        (CLASS, 'Class'),
        (HOME, 'Home'),
        (WORK, 'Work'),
    )

    address = AddressField(
        on_delete=models.CASCADE,
    )

    location_type = models.CharField(
        db_column="type",
        choices=LOCATION_TYPE_CHOICES,
        default=HOME,
        max_length=1,
    )

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        """Unicode representation of Location."""
        location_type = dict(self.LOCATION_TYPE_CHOICES).get(self.location_type)
        return f'({location_type}) {self.address}'
