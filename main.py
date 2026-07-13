from crud.create_table import create_users_table
from crud.insert import create_user
def main():
    create_users_table()
    # create_user(2,'Akita')
    create_user(3,"Sania")
if __name__=="__main__":
    main()