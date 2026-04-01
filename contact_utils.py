def add_contact(contacts, name, phone):
    contact = {
        "name": name,
        "phone": phone
    }
    contacts.append(contact)
    return contacts


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")


def search_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            return True
    return False