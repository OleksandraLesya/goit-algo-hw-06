"""
This module defines the AddressBook class, which manages a collection of contact records.
It uses UserDict to provide dictionary-like behavior for storing records.
"""

from collections import UserDict
from .record import Record # Імпортуємо клас Record з файлу record.py


class AddressBook(UserDict):
    """
    Represents an address book that stores and manages contact records.
    Inherits from UserDict to use dictionary-like behavior.
    """
    def add_record(self, record: Record):
        """
        Adds a new record to the address book.
        The record's name value is used as the key.

        Args:
            record (Record): The Record object to add.
        """
        self.data[record.name.value] = record
        print(f"Record for {record.name.value} added to the address book.")

    def find(self, name: str):
        """
        Finds a record in the address book by contact name.

        Args:
            name (str): The name of the contact to find.

        Returns:
            Record or None: The Record object if found, otherwise None.
        """
        return self.data.get(name)

    def delete(self, name: str):
        """
        Deletes a record from the address book by contact name.

        Args:
            name (str): The name of the contact to delete.
        """
        if name in self.data:
            del self.data[name]
            print(f"Record for {name} deleted from the address book.")
        else:
            print(f"Record for {name} not found in the address book.")

    def __str__(self):
        """
        Returns a string representation of the entire address book.
        Each record's __str__ method is used for formatting.
        """
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())
