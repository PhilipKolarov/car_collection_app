from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def username_length_validator(string):
    if len(string) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


def year_value_validator(year):
    if year > 2049 or year < 1980:
        raise ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MAX_LENGTH_PASSWORD = 30
    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30
    MIN_VALUE_AGE = 18

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            username_length_validator,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(MIN_VALUE_AGE)
        ],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    MAX_LENGTH_TYPE = 10
    MAX_LENGTH_MODEL = 20
    MIN_LENGTH_MODEL = 2
    MIN_VALUE_PRICE = 1

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LENGTH_MODEL,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_MODEL)
        ],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=[
            year_value_validator,
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_VALUE_PRICE)
        ],
        null=False,
        blank=False,
    )
