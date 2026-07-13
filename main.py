# from crud.create_table import create_users_table
# from crud.insert import create_user
# def main():
#     create_users_table()
#     # create_user(2,'Akita')
#     create_user(3,"Sania")
# if __name__=="__main__":
#     main()
# main.py

from crud.insert import create_user
# from crud.read import get_user
# from crud.update import update_user
# from crud.delete import delete_user
from crud.create_table import create_users_table  # Import the new table creation function

def main():
    #Create the users table if it doesn't exist
    create_users_table()

    # Example CRUD operations:
    # Create a new user
    create_user(4, 'Snigdha')

    # # Read user data
    #get_user(1)

    # # Update user data
    #update_user(1, 'john1_doe_updated')

    # # Delete the user
    #delete_user(1)

if __name__ == "__main__":
    main()