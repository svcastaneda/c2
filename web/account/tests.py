from django.test import TestCase
from django.utils import timezone

from .models import (
    User,
    Email,
    Phone,
    Gender,
)


def create_user():
    return User(
        email="test@test.com",
        password="thisisapassword",
        date_of_birth=timezone.datetime(year=2000, month=5, day=6),
    )


class UserModelTest(TestCase):

    def test_age_no_date(self):
        """
        Test if no date passed to `age()` will work still, using today's date.
        """

        now = timezone.now()
        year = now.year - 10
        month = now.month
        day = now.day

        user = create_user()
        user.date_of_birth = timezone.datetime(
            year=year, month=month, day=day
        )

        # 10 years later
        age = user.age()

        self.assertEqual(age, 10)

    def test_age(self):
        """
        Test to make sure user is 10 years old.
        """

        user = create_user()

        # One day before 10 years old
        age = user.age(
            date=timezone.datetime(2010, 5, 5)
        )

        self.assertEqual(age, 9)


class EmailModelTest(TestCase):
    def test_string_representation(self):
        user = create_user()

        email = Email(
            user=user,
            address="work@test.com",
        )

        self.assertEqual(
            str(email),
            email.address
        )

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Email._meta.verbose_name_plural),
            "Email Addresses"
        )


class PhoneModelTest(TestCase):

    def test_string_representation(self):
        user = create_user()

        phone = Phone(
            user=user,
            number="+1 555-555-5555",
        )

        self.assertEqual(
            str(phone),
            f"{phone.number}"
        )

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(Phone._meta.verbose_name_plural),
            "Phone Numbers"
        )


class GenderModelTest(TestCase):

    def test_string_representation(self):
        gender = Gender(
            gender="Male",
            referred_to_as="Male"
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
