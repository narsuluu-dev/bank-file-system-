# Welcome!  


import user 


print("Welcome to FileBank System!")  

print("1. Create Account") 
print("2. Log In")
print("3. Exit")  

user = input("Enter your choice: ") 

if user == "1": 
    print("Creating a new account...")
    

elif user == "2":
    create_account()

elif user ==  "3":
    print("Thank you for using FileBank. Goodbye! ") 

    exit()

else: 
    print("Invalid input. Please choose 1, 2 or 3. ") 



