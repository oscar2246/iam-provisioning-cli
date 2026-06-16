
import user_ops
import storage
def menu():

    storage.initialize_file()

    while True:
        print("\n --- Menu --- ")
        print("1. Create user")
        print("2. List users")
        print("3. Disable user")
        print("4. Enable user")
        print("5. Search User")
        print("6. Exit")
        
        try:
            user_choice = int(input("Input choice here: "))
        except ValueError:
            print("Input a number choice please, try again")
            continue
            
        if user_choice == 1:
            user_ops.create_user()
        elif user_choice == 2:
            user_ops.list_users()
        elif user_choice == 3:
            user_ops.disable_user()
        elif user_choice == 4:
            user_ops.enable_user()
        elif user_choice == 5:
            user_ops.search_user()
        elif user_choice == 6:
            print("Goodbye")
            break
        else:
            print("Not a valid choice")

menu()