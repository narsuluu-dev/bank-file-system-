import user 

def check_balance(username):

    with open(f"{username}.txt", "r") as file:
        balance = file.read()
        return float(balance)
    

def deposit(username, amount): 

    with open(f"{username}.txt", "r") as file: 
        balance = float(file.read())
        balance += amount   
 
    
        

    with open (f"{username}.txt", "w") as file:  
        file.write(str(balance))  
        

          

def withdraw(username, amount): 
    
    with open(f"{username}.txt", "r") as file:  
        balance = float(file.read())

        if balance >= amount:
            balance -= amount 

            with open(f"{username}.txt", "w") as file: 
               file.write(str(balance)) 
            print("Withdrawal is successful. New balance", balance)

        else:  
            print("Insufficient funds ") 




username = input("Enter your username: ")
action = input("Do you want to deposit, withdraw, or check balance?").lower()

if action == "deposit": 
    amount = float(input("Enter amount to deposit: "))
    deposit(username, amount)

elif action == "withdraw": 
     amount = float(input("Enter amount to withdraw: ")) 
     withdraw(username, amount)

elif action == "check balance ": 
    print(f"Your balance is: {check_balance(username)}")

else: 
    print("Invalid action")


      


  










        






