import os 


def create_account(username): 
    
    filename = f"{username}.txt" 

    # check if the file alreasy exsists 

    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("0.0") # Initial balance  


def read_balance(username):

    filename = f"{username}.txt"

    try: 
        with open("filename", "r") as file: 
            balance  = float(file.read()) 
            return balance 
        
    except FileNotFoundError:
        print("File is not found")
        return None 
    



    






 