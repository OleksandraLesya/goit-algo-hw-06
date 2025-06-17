Virtual Assistant - Address Book System
This repository contains a Python implementation of an address book using object-oriented programming (OOP) principles. It includes custom classes for managing contacts, validating phone numbers, and organizing records in a structured and extensible way.

Features
Store contact names and multiple phone numbers

Add, edit, delete, and search phones in a contact

Add and remove full contact records

Validate phone numbers (must be 10 digits)

Easily extendable for future features (email, birthdays, etc.)

Project Structure
Field
Base class for all fields in a contact. Stores the field's value and provides a string representation.

Name
Inherits from Field. Used to represent a contact's name. Required field.

Phone
Inherits from Field. Represents a phone number. Includes validation (must contain exactly 10 digits).

Record
Stores information about a single contact:

A Name object

A list of Phone objects

Methods for adding, editing, removing, and finding phones

AddressBook
Inherits from UserDict. Manages a collection of Record objects. Provides methods to:

Add new records

Find records by name

Delete records by name

Display all records in a formatted way

How to Run the Demonstration
To run the demonstration of the address book functionality:

Ensure you are in the root directory of the repository (goit-algo-hw-06/).

Execute the following command in your terminal:

python -m HW6.assistant_bot.main

This command will run main.py as a module, allowing Python to correctly recognize the internal package structure.

Example Usage
from HW6.assistant_bot.record import Record
from HW6.assistant_bot.address_book import AddressBook
from HW6.assistant_bot.fields import Name, Phone # Including these for completeness of example

# Create a new address book
book = AddressBook()

# Create a contact for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

# Create and add another contact
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all contacts
print("\n--- All contacts ---") # Added for clearer output in example
print(book)

# Edit a phone number for John
john = book.find("John")
if john: # Added check as find can return None
    try:
        john.edit_phone("1234567890", "1112223333")
        print("\n--- John's record after editing ---") # Added for clearer output
        print(john)
    except ValueError as e:
        print(f"Error editing John's phone: {e}")
else:
    print("John not found.")


# Find a phone
if john: # Added check as john might be None
    found_phone = john.find_phone("5555555555")
    print(f"\n--- Found phone for John ---") # Added for clearer output
    print(f"{john.name}: {found_phone}")
else:
    print("John's record not available for phone search.")


# Delete Jane's record
book.delete("Jane")
print("\n--- After deleting Jane ---") # Added for clearer output
print(book)

Author
Created with ❤️ by OleksandraLesya
