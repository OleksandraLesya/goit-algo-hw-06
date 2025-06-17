"""
This module serves as the main entry point for demonstrating the AddressBook functionality.
It showcases how to create an AddressBook, add records, manage phone numbers within records,
and perform searches and deletions.
"""

from .record import Record
from .address_book import AddressBook


if __name__ == "__main__":
    # Create a new address book
    book = AddressBook()

    # Create a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John's record to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Display all records
    print("\nУся адресна книга:")
    print(book)

    # Find and edit John's phone
    john = book.find("John")
    if john: # Додаємо перевірку, бо find може повернути None
        john.edit_phone("1234567890", "1112223333")
        print("\nПісля редагування телефону у John:")
        print(john)
    else:
        print("Контакт John не знайдено для редагування.")

    # Search for a phone
    if john: # Додаємо перевірку, бо john може бути None
        found_phone = john.find_phone("5555555555")
        print(f"\nЗнайдено телефон у John: {found_phone}")
    else:
        print("Контакт John не доступний для пошуку телефону.")


    # Delete Jane's record
    book.delete("Jane")
    print("\nПісля видалення Jane:")
    print(book)
