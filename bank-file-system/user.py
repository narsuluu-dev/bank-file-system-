
def create_account(): 
    print("Creating a new account...") 

    user_name = input("Enter a name: ")
    password = input("Create a password: ") 

    with open("user_data.txt", "a") as file: 
        file.write(f"{user_name}, {password}\n")  

    print("Account has been created successfully!")

    return user_name, password 




def log_in():  
     
    user_name = input("Enter your username: ") 
    password  = input("Enter your password: ")  

    
    with open ("user_data.txt", "r") as file: 
        for line in file: 
            saved_name, saved_pass = line.strip().split(",")
            





create_account()
log_in() 








    






    