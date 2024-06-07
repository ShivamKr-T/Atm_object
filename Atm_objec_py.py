class Atm:
    
    def __init__(self):
        
        self.__pin=""
        self.__balance=0
        
        self.__menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self,new):
        if type(new)==str:
            self.__pin=new
            print("PIN changed")
        else:
            print("Not allowed")
        
    def __menu(self):
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
        self.__pin=input("Enter your pin:")
        print("PIN set succesfully")
        
    def deposit(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            amount=int(input("Enter the amount you want to deposit:"))
            self.__balance+=amount
            print("Deposit succesful")
        else:
            print("Invalid PIN")
            
    def withdraw(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            amount=int(input("Enter the amount you want to deposit:"))
            if amount<=self.__balance:
                self.__balance-=amount
                print("Money withdrawn")
            else:
                print("Insufficient money")
        else:
            print("Invalid PIN")
            
    def check_balance(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            print("Your remaining balance is",self.__balance)
        else:
            print("Invalid PIN")
        
        
        
