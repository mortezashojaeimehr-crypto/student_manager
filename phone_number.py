import sys
import io
import os
import json

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
contacts={}

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists("contacts.json"):
    with open("contacts.json","r",encoding="utf-8")as f:
        contacts=json.load(f)
        

def save_contact():
    with open("contacts.json","w",encoding="utf-8")as f:
        json.dump(contacts,f,ensure_ascii=False,indent=4)

def show_menu(seperator="_",length=40):
    print("\n"+seperator*length)
    print("phone_numbers")
    print(seperator*length)
    print("1.insert contact")
    print("2.edit contact")
    print("3.show contacts")
    print("4.search contact")
    print("5.delete contact")
    print("6.exit")
while True:
    show_menu()
    choice = input("select one mission\n")

    if choice=="1":
        name = input("name:\n")
        phone = input("phone number:\n")
        contacts[name]=phone
        save_contact()
        print("The contact saved successfully")

    elif choice == "2":
        name = input("Insert the contact name\n")
        if name in contacts:
            new_phone= input("Insert the new number\n")
            contacts[name]=new_phone
            save_contact()
            print(f"The number of {name} changed to {new_phone} ")
        else:
            print("The contact not found.")

    elif choice == "3":
        if not contacts:
            print("no contacts")
        else:
            print("contacts list: \n")
            for name , phone in contacts.items():
                print(f"{name}:{phone}")

    elif choice=="4":
        name = input("insert a name for search\n")
        if name in contacts:
            print(f"name:{name}  number:{contacts[name]}")
        else:
            print("The contact not found.")

    elif choice=="5":
        name = input("insert a name for delete:\n")
        if name in contacts:
            del contacts[name]
            save_contact()
            print(f"{name} deleted successfully")
        else:
            print("The contact not found.")

    elif choice == "6":
        print("Good bye")
        break

    else:
        print("Please insert a number from 1 to 6")





