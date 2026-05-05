
import json
import os

data_file = "data.json"

def load_users():
    if not os.path.exists(data_file):
        return []
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return[]

def save_users(users):
    with open(data_file, "w") as f:
        json.dump(users, f, indent=4)


def initialize_file():

    if not os.path.exists(data_file):
        save_users([])

def create_user():
    print("\n --- User Creation --- ")
        
    users = load_users()

    #User information gathering
    f_name = input("Enter First Name: ").strip()
    m_name = input("Enter Middle Name: ").strip()
    l_name = input("Enter Last Name: ").strip()

    if not f_name or not l_name:
        print("Error first and last name required")
        return 

    #Gathering existing Emails & LANID

    exiting_lan_ids = [user['LANID'].upper() for user in users]
    existing_emails = [user['Email'].lower() for user in users]

    #LANID generation
    base_lan_id = (f"{f_name[:4]}{m_name[:1]}{l_name[:2]}").upper()
    LANID = base_lan_id
    l_counter = 1 
    while LANID in exiting_lan_ids:
        LANID = (f"{base_lan_id}{l_counter}")
        l_counter += 1

    #Email generation    
    base_email_local = (f"{f_name}.{l_name}")
    domain = "@example.internal"
    email = (f"{base_email_local}{domain}")
    e_counter = 1

    while email in existing_emails:
        #if John.doe@example.internal exists then it will use john.doe1@example.internal, avoiding collision
        email = (f"{base_email_local}{e_counter}{domain}")
        e_counter += 1

    #grouping all new user information
    new_user = {"Last Name":l_name,
                "First Name":f_name,
                "Middle Name":m_name,
                "Email":email,
                "LANID":LANID
    }

    users.append(new_user)
    save_users(users)

    m_inital = m_name[0] if m_name else""

    print(f"\nSuccessfully Created account for {l_name}, {f_name} {m_name[:1]}.")
    print(f"Email: {email}")
    print(f"LANID: {LANID}")

def list_users():
    print(" --- Users --- ")
    users = load_users()
    if not users:
        print("No users found.")
        return

    for i, user in enumerate(users, 1):
        print(f"{i}. {user['Last Name']}, {user['First Name']} | LANID: {user['LANID']} | Email: {user['Email']}")
def delete_user():
    print(" --- Delete User --- ")

def menu():
    initialize_file()
    
    while True:
        print("\n --- Menu --- ")
        print("1. Create User")
        print("2. List Users")
        print("3. Delete user")
        print("4. Exit")

        try:
            user_choice = int(input("Input choice here: "))
        except ValueError:
            print("Input a number choice please, try again")
            continue

        if user_choice == 1:
            create_user()
            
        elif user_choice == 2:
            list_users()

        elif user_choice == 3:
            delete_user()

        elif user_choice == 4:
            print("Goodbye")
            break
        else:
            print("Not a valid choice")
   
menu()
