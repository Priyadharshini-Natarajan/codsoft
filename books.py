#To store contact details and to manipulate it

contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone_number": phone_number,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    print("\nContact List:")
    for index, contact in enumerate(contacts, start=1):
        print(str(index) + ". Name: " + contact['name'] + ", Phone: " + contact['phone_number'])


def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone_number']:
            print("Contact found:")
            print_contact(contact)
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    search_query = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']:
            print("Contact found:")
            print_contact(contact)
            choice = input("What would you like to update? (name/phone/email/address): ")
            new_value = input(f"Enter new {choice}: ")
            contact[choice] = new_value
            print("Contact updated successfully!")
            print_contact(contact)
            return
    print("Contact not found.")

def delete_contact():
    search_query = input("Enter name or phone number of the contact to delete: ")
    for index, contact in enumerate(contacts):
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone_number']:
            print("Contact found:")
            print_contact(contact)
            confirmation = input("Are you sure you want to delete this contact? (yes/no): ")
            if confirmation.lower() == "yes":
                del contacts[index]
                print("Contact deleted successfully!")
            return
    print("Contact not found.")

def print_contact(contact):
    print("Name: " + contact['name'])
    print("Phone: " + contact['phone_number'])
    print("Email: " + contact['email'])
    print("Address: " + contact['address'])



def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
