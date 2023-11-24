from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Model representing user profiles.

    Attributes:
    - user (OneToOneField): The associated user object.
    - favorite_city (CharField): The favorite city of the user.
    
    Methods:
    - __str__(): Returns a string representation of the user's profile.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the user's profile.

        Example:
        "john_doe_profile"
        """
        return self.user.username

