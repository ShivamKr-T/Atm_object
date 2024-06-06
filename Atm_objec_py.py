class Atm:
    
    def __init__(self):
        
        self.pin=""
        self.balance=0
        
        self.menu()
        
    def menu(self):
        user_input=int(input("""
                         Hello how would you like to proceed?
                         1.Enter 1 to create pin
                         2.Enter 2 to deposit
                         3.Enter 3 to withdraw
                         4.Enter 4 to check balance
                         5.Enter 5 to exit
                         """))
        
        if user_input==1:
            self.create_pin()
           
        elif user_input==2:
            self.deposit()
            
        elif user_input==3:
            self.withdraw()
            
        elif user_input==4:
            self.check_balance()
            
        else:
            print("Have a nice day :)")
        
    def create_pin(self):
        self.pin=input("Enter your pin:")
        print("PIN set succesfully")
        
    def deposit(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            amount=int(input("Enter the amount you want to deposit:"))
            self.balance+=amount
            print("Deposit succesful")
        else:
            print("Invalid PIN")
            
    def withdraw(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            amount=int(input("Enter the amount you want to deposit:"))
            if amount<=self.balance:
                self.balance-=amount
                print("Money withdrawn")
            else:
                print("Insufficient money")
        else:
            print("Invalid PIN")
            
    def check_balance(self):
        temp=input("Enter your pin:")
        if temp==self.pin:
            print("Your remaining balance is",self.balance)
        else:
            print("Invalid PIN")
        
        
        
