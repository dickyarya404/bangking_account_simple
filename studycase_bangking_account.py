class Account:
    def __init__(self):
        self.balance = 0
        print("New Account is created")

    def deposit(self):
        amount = float(input('Enter amount to be deposited: '))
        self.balance += amount
        print("New Balance is: ", self.balance)

    def withdraw(self):
        amount = float(input('Enter amount to withdraw: '))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("New Balance is: ", self.balance)

    def enquiry(self):
        print("Balance is: ", self.balance)

# Create an account and perform operations
ac = Account()
ac.deposit()
ac.withdraw()
ac.enquiry()
