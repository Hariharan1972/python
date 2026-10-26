import json
from pathlib import Path

FILE = Path("contacts.json")


def load_contacts():
    if FILE.exists():
        try:
            return json.loads(FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not load contacts.")
    return {}


def main():
    contacts = load_contacts()

    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()

            if not name or not phone:
                print("Name and phone are required.")
                continue

            contacts[name] = phone
            FILE.write_text(
                json.dumps(contacts, indent=4),
                encoding="utf-8"
            )
            print("Contact saved.")

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            phone = contacts.get(name)

            if phone:
                print(f"{name}: {phone}")
            else:
                print("Contact not found.")

        elif choice == "3":
            if contacts:
                for name, phone in sorted(contacts.items()):
                    print(f"{name}: {phone}")
            else:
                print("No contacts saved.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
