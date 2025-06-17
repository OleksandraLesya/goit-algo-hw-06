"""
This module defines the Record class, which represents a single contact entry.
It manages a contact's name and a list of phone numbers.
"""

from .fields import Name, Phone # Import Name and Phone classes from fields.py


class Record:
    """
    Class representing a contact record.
    Contains a Name object and a list of Phone objects.
    """

    def __init__(self, name: str):
        """
        Initialize a Record with a name and an empty list of phones.

        Args:
            name (str): The name of the contact.
        """
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number: str):
        """
        Adds a new phone number to the contact's list of phones.

        Args:
            phone_number (str): The phone number to add.
        """
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str):
        """
        Removes a phone number from the contact's list of phones.

        Args:
            phone_number (str): The phone number to remove.

        Raises:
            ValueError: If the phone number is not found in the contact's phones.
        """
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            print(f"Phone {phone_number} removed from {self.name.value}.")
        else:
            raise ValueError(f"Phone number {phone_number} not found.")

    def edit_phone(self, old_number: str, new_number: str):
        """
        Edits an existing phone number for the contact.

        Args:
            old_number (str): The existing phone number to replace.
            new_number (str): The new phone number.

        Raises:
            ValueError: If the old phone number is not found or the new phone number is invalid.
        """
        phone_to_edit = self.find_phone(old_number)
        if phone_to_edit:
            self.phones.remove(phone_to_edit)
            try:
                self.phones.append(Phone(new_number))
                print(f"Phone {old_number} changed to {new_number} for {self.name.value}.")
            except ValueError as e:
                self.phones.append(phone_to_edit)
                raise ValueError(f"Invalid new phone number: {e}") from e
        else:
            raise ValueError(f"Old phone number {old_number} not found.")

    def find_phone(self, phone_number: str) -> Phone | None:
        """
        Finds a Phone object by its number in the contact's list of phones.

        Args:
            phone_number (str): The phone number to search for.

        Returns:
            Phone: The Phone object if found, otherwise None.
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        """
        Returns a string representation of the contact record.
        """
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"
