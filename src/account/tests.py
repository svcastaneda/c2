from django.test import TestCase
from django.utils import timezone

from .models import Gender, User


class GenderModelTest(TestCase):

    def test_string_representation(self):
        gender = Gender(
            gender="Male",
            referered_as="Male"
        )

        self.assertEqual(
            str(gender),
            gender.gender
        )

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Gender._meta.verbose_name_plural),
            "Genders"
        )


class UserModelTest(TestCase):

    def create_user(self):
        pass

    def test_age_no_date(self):
        """
        Test if no date passed to `age()` will work still, using today's date.
        """

        now = timezone.now()
        year = now.year - 10
        month = now.month
        day = now.day

        user = User(
            email="test@test.com",
            password="thisisapassword",
            date_of_birth=timezone.datetime(year=year, month=month, day=day),
        )

        # 10 years later
        age = user.age()

        self.assertEqual(age, 10)

    def test_age(self):
        """
        Test to make sure user is 10 years old.
        """

        user = User(
            email="test@test.com",
            password="thisisapassword",
            date_of_birth=timezone.datetime(year=2000, month=5, day=6),
        )

        # One day before 10 years old
        age = user.age(
            date=timezone.datetime(2010, 5, 5)
        )

        self.assertEqual(age, 9)
