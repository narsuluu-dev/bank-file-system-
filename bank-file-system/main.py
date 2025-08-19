# Welcome! 


print("Welcome to FileBank System!") 
print("Chose an option: ") 

print("1. Create Account") 
print("2. Log In")
print("3. Exit") 
print("4. Check balance")   
print("5. Deposit") 
print("6. Withdraw")



from user import create_account , log_in
from banking import check_balance , deposit, withdraw

user = input("Enter your choice: ") 

if user == "1": 
    create_account()
    

elif user == "2":
    log_in()

elif user ==  "3":
    print("Thank you for using FileBank. Goodbye! ") 

    exit() 

elif user == "4":
    check_balance() 

elif user == "5":
    deposit()

elif user == "6":
    withdraw() 

else: 
    print("Invalid input. Please choose 1, 2 or 3. ") 



