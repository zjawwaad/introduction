class BankAccount:
    def __init__(self, int_rate= 0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds") 
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self

class User: 
    def __init__(self, name, balance): 
        self.name= name
        self.account = BankAccount()


        # self.account = BankAccount

zaynah=User("Zaynah", 0)


jim=User("Zaynah", 0)


zaynah.account.deposit(20), zaynah.account.deposit(50), zaynah.account.deposit(60), zaynah.account.withdraw(30), zaynah.account.yield_interest()

zaynah.account.display_account_info()


jim.account.deposit(30), jim.account.deposit(85), jim.account.deposit(5), jim.account.withdraw (130),jim.account.yield_interest()
jim.account.display_account_info()
