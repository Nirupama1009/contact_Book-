def add_contact(name, number):
    with open("contacts.txt", "a") as file:
        file.write(f"{name} - {number}\n")
    print("Contact saved!")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            print("\n--- Contacts ---")
            print(file.read())
    except FileNotFoundError:
        print("No contacts found.")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
