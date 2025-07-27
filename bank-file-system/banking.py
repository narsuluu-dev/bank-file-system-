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




user = input("Enter your username: ")
amount = float(input("Enter amount to deposit: "))
deposit(user, amount)




      


  










        






