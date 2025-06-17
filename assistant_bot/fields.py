"""
This module defines the base Field class and its derivatives Name and Phone.
These classes are used to represent different types of data fields within a contact record.
"""
class Field:
    """Base class for all fields in a contact record."""

    def __init__(self, value):
        """
        Initialize a Field with the given value.

        Args:
            value: The value to be stored in the field.
        """
        self.value = value

    def __str__(self):
        """Return a string representation of the field value."""
        return str(self.value)


class Name(Field):
    """Class to store the contact's name. Inherits from Field."""
    pass # <-- Тепер цей 'pass' має бути без підкреслення


class Phone(Field):
    """Class to store a phone number with 10-digit validation."""

    def __init__(self, value):
        """
        Initialize a Phone object and validate the number.

        Args:
            value (str): The phone number as a string.

        Raises:
            ValueError: If the number is not 10 digits long or contains non-digit characters.
        """
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)

