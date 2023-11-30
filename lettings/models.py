from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.

    Attributes:
    - number (PositiveIntegerField): The street number.
    - street (CharField): The street name.
    - city (CharField): The city name.
    - state (CharField): The state abbreviation.
    - zip_code (PositiveIntegerField): The ZIP code.
    - country_iso_code (CharField): The ISO code of the country.

    Meta:
    - verbose_name: Singular name for the model in the Django admin.
    - verbose_name_plural: Plural name for the model in the Django admin.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Returns a string representation of the address.

        Example:
        "123 Main St"
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Represents a letting (rental) with a title and associated address.

    Attributes:
    - title (CharField): The title of the letting.
    - address (OneToOneField): The associated address for the letting.

    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the letting.

        Example:
        "Cozy Apartment in the City"
        """
        return self.title
