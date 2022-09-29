from bank_accounts import BankAccount

class User: 
    def __init__(self, name, email): 
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.02, balance=0)

    def deposit(self, amount):
        self.account.deposit(amount)

    def withdraw(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f" {self.name} Balance: $ {self.balance}")
        return self

kevin=User ("Kevin", "kev@me.com")
nisha=User ("Nisha", "nish@me.com")

kevin.deposit(40) 
kevin.account.display_account_info()


