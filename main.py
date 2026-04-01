from contact_utils import add_contact, view_contacts, search_contact, delete_contact


def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def get_user_choice():
    return input("Enter your choice: ")


def handle_choice(choice, contacts):
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        add_contact(contacts, name, phone)
        print("Contact added successfully!")

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        name = input("Enter name to search: ")
        result = search_contact(contacts, name)
        if result:
            print(f"Found: {result['name']} - {result['phone']}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        deleted = delete_contact(contacts, name)
        if deleted:
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting program...")
        return False

    else:
        print("Invalid choice. Try again.")

    return True


def main():
    contacts = []
    running = True
    while running:
        display_menu()
        choice = get_user_choice()
        running = handle_choice(choice, contacts)


main()