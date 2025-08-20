# Welcome!


print("Welcome to FileBank System!") 
print("Chose an option: ") 

print("1. Create Account") 
print("2. Log In")
print("3. Exit") 
print("4. Check balance")   
print("5. Deposit") 
print("6. Withdraw")


user = input("Enter your choice: ") 

if user == "1":  
    from user import create_account 
    create_account()
    
    
    

elif user == "2": 
    from user import log_in 
    log_in() 
 


elif user ==  "3":
    print("Thank you for using FileBank. Goodbye! ") 

    exit() 

elif user == "4":
    from banking import check_balance  
    username = input("Enter your username to check balance: ") 
    check_balance(username)  
 
elif user == "5":
    from banking import deposit  
    username = input("Enter your username to deposit: ")
    amount = float(input("Enter amount to deposit: "))
    deposit(username, amount) 

elif user == "6":
    from banking import withdraw  
    username = input("Enter your username to withdraw: ")
    amount = float(input("Enter amount to withdraw: "))  
    withdraw(username, amount) 

else: 
    print("Invalid input. Please choose 1, 2 or 3. ")  

    



