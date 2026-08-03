contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add Contact
    if choice == 1:

        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        if name in contacts:
            print("Contact already exists!")
        else:
            contacts[name] = phone
            print("Contact added successfully.")

    # Display Contacts
    elif choice == 2:

        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)

    # Search Contact
    elif choice == 3:

        name = input("Enter name to search: ")

        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")

    # Update Contact
    elif choice == 4:

        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == 5:

        name = input("Enter name to delete: ")

        if name in contacts:
            contacts.pop(name)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Exit
    elif choice == 6:

        print("Thank you!")
        break

    else:
        print("Invalid choice!")