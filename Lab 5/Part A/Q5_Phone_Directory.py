
contacts = {
    "Anita": {
        "phones": ["9876543210"],
        "email": "anita@mail.com",
        "city": "Pune"
    },
    "Manoj": {
        "phones": ["9123456780", "9988776655"],
        "email": "manoj@mail.com",
        "city": "Delhi"
    },
    "Zara": {
        "phones": ["9000011111"],
        "email": "zara@mail.com",
        "city": "Pune"
    }
}


# Validate phone number
def valid_phone(number):
    return len(number) == 10 and number.isdigit()


# Check whether a number belongs to another contact
def number_exists(number, name):
    for contact, data in contacts.items():
        if contact != name and number in data["phones"]:
            return True
    return False


# 1. Add contact
def add_contact():
    name = input("Enter name: ").strip()

    if name in contacts:
        print("Contact already exists.")
        return

    number = input("Enter 10-digit phone number: ").strip()

    if not valid_phone(number):
        print("Rejected: Phone number must contain exactly 10 digits.")
        return

    if number_exists(number, name):
        print("Rejected: Number already belongs to another contact.")
        return

    email = input("Enter email: ")
    city = input("Enter city: ")

    contacts[name] = {
        "phones": [number],
        "email": email,
        "city": city
    }

    print("Contact added successfully.")


# 2. Add another number
def add_number():
    name = input("Enter contact name: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    number = input("Enter new phone number: ").strip()

    if not valid_phone(number):
        print("Rejected: Phone number must contain exactly 10 digits.")
        return

    if number in contacts[name]["phones"]:
        print("Number already exists for this contact.")
        return

    if number_exists(number, name):
        print("Rejected: Number belongs to another contact.")
        return

    contacts[name]["phones"].append(number)
    print("Phone number added successfully.")


# 3. Update email or city
def update_contact():
    name = input("Enter contact name: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("1. Update email")
    print("2. Update city")

    choice = input("Enter choice: ")

    if choice == "1":
        contacts[name]["email"] = input("Enter new email: ")
        print("Email updated successfully.")

    elif choice == "2":
        contacts[name]["city"] = input("Enter new city: ")
        print("City updated successfully.")

    else:
        print("Invalid choice.")


# 4. Delete contact
def delete_contact():
    name = input("Enter contact name: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


# 5. Search
def search_contact():
    print("1. Search by partial name")
    print("2. Reverse lookup by phone number")

    choice = input("Enter choice: ")

    if choice == "1":
        search_name = input("Enter name to search: ").lower()

        found = False

        for name, data in contacts.items():
            if search_name in name.lower():
                print(name, data)
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "2":
        number = input("Enter phone number: ").strip()

        # Build number -> name dictionary using comprehension
        reverse = {
            phone: name
            for name, data in contacts.items()
            for phone in data["phones"]
        }

        if number in reverse:
            print("Number belongs to:", reverse[number])
        else:
            print("Number not found.")

    else:
        print("Invalid choice.")


# 6. Reports
def reports():
    # Contacts grouped by city
    city_groups = {}

    for name, data in contacts.items():
        city = data["city"]
        city_groups.setdefault(city, []).append(name)

    for city in city_groups:
        city_groups[city].sort()

    print("\n1. Contacts grouped by city:")
    print(city_groups)

    # Contacts having more than one number
    multiple_numbers = {
        name: data["phones"]
        for name, data in contacts.items()
        if len(data["phones"]) > 1
    }

    print("\n2. Contacts with more than one number:")
    print(multiple_numbers)

    # Print entire directory alphabetically
    print("\n3. Complete Phone Directory:")

    for name in sorted(contacts):
        data = contacts[name]
        print("Name:", name)
        print("Phones:", data["phones"])
        print("Email:", data["email"])
        print("City:", data["city"])
        print()


# Main menu
while True:
    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Add Another Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        add_number()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        search_contact()
    elif choice == "6":
        reports()
    elif choice == "7":
        print("Exiting Phone Directory.")
        break
    else:
        print("Invalid choice.")
