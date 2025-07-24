def create_account(): 
    print("Creating a new account...") 

    user_name = input("Enter a name: ")
    password = input("Create a password ") 

    with open("user_data.txt", "a") as file: 
        file.write(f"{user_name}, {password}\n")

    print("Account has been created successfully!")

d



    