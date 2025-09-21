import json

FILENAME = "contacts.json"

try:
    with open(FILENAME, "r") as file:
        contact_list = json.load(file)
except FileNotFoundError:
    contact_list = {"emergency": "911"}

def save_contacts():
    with open(FILENAME, "w") as file:
        json.dump(contact_list, file, indent=4)


# contact_list = {
#     "emergency " : 911
# }

def add_contact(name, number):
    contact_list[name] = number
    save_contacts()

def delete_contact(name):
    if name in contact_list:
        contact_list.pop(name)
    else:
        print("This contact is not register")

def update_contact(name,number):
    if name in contact_list:
        contact_list[name] = number
    else:
        print("This name doesn't exist")

def show_all_contact():
    for name,number in contact_list.items():
        print(f"{name} : {number}")

def show_a_contact(name):
    if name in contact_list:
        print(f"{contact_list[name]}")
    else:
        print("This contact is not register")

working = True

while working:
    print('''
        welcome in the contact list app, select your option : 
        1 - add a contact
        2 - see all conatact
        3 - delete a contact
        4 - see one contact
        5 - modify a number
        6 - quit the program
        ''')
    try :
        entry = int(input("Enter your option : "))
        if entry == 6:
            print("You are quitting the program, thank for using our services")
            working = False
        elif entry == 1:
            name = input("Enter the name of the new contact : ")
            number = input("Enter the number of the new contact : ")
            add_contact(name, number)
            print("Contact added succefully!")
        elif entry == 2:
            show_all_contact()
        elif entry == 3:
            name = input("Enter the name of the contact you want to delete : ").lower()
            delete_contact(name)
            print("Number delete succefully!")
        elif entry == 4:
            name = input('please enter the name of the number you want to see : ')
            show_a_contact(name)
        elif entry == 5:
            name = input("Please enter the name of the number to modify : ")
            number = input("please enter the new number : ")
            update_contact(name, number)
    except ValueError:
        print("Your entry is invalid, please try again")





