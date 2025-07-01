# Bank Management System Project

class Account():
    def __init__(self,name="",password="",balance=0):
        self.name = name
        self.password = password
        self.balance = balance
    def create_account(self):
        print("---- Welcome to Python Bank ----")
        self.name = input("Enter your name: ")
        self.password = input("Enter your password: ")
        print("Account created successfully!")
    def login(self):
        print("---- Login ----")
        name_input = input("Enter your name: ")
        password_input = input("Enter your password: ")
        if name_input == self.name and password_input == self.password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials. Please enter the right credentials")
            return False

    def ExitApp(self):
        print("Bye")
        exit()
    def Deposit(self):
        amount = float(input("Enter the deposit amount:"))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self.balance}")
        else:
            print("Amount must be positive.")
    def Withdraw(self):
        amount1 = float(input("Enter the withdrawal amount:"))
        if 0 < amount1 <= self.balance:
            self.balance -= amount1
            print(f"₹{amount1} withdrawn. New Balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
    def check_balance(self):
        print(f"Your current balance is {self.balance}")
    def Logout(self):
        print("You logged of sussessfully")
        exit()

acc = Account()

while True:
    print("---Welcome to Python Bank---")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    choice = int(input("Enter your choice (1-3):"))
    if choice == 1:
        acc.create_account()
    elif choice == 2:
        if acc.login():
         while True:
            print("1.Deposit")
            print("2.Withdraw")
            print("3.Check Balance")
            print("4.Logout")
            choice1 = int(input("Enter your choice (1-4): "))
            if choice1 == 1:
                acc.Deposit()
            elif choice1 == 2:
                acc.Withdraw()
            elif choice1 == 3:
                acc.check_balance()
            elif choice1 == 4:
                acc.Logout()
                break  
            else:
                print("Invalid option. Please enter between 1-4.")
            
    elif choice == 3:
        acc.ExitApp()
    else:
        print("Invalid option please enter between (1-3):")







        



    
        