class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(name=User, int_rate=0.02, account_balance=0)
    def make_deposit(self, amount):
        self.account_balance.make_deposit(amount)
        return self
    def make_withdrawal(self, amount):

            self.account_balance.withdraw(amount)


            return self

class BankAccount:
        def __init__(self,name,int_rate,account_balance):

            self.account_balance = account_balance
            self.int_rate = int_rate
            self.name = name

        def make_deposit(self, amount):
            self.account_balance += amount
            return self

        def withdraw(self, amount):
            self.account_balance -= amount
            return self

        def yield_interest(self):
            if self.account_balance > 0:
                self.account_balance = self.account_balance * self.int_rate + self.account_balance
                return self
        def display_account_info(self):
            return self.account_balance





Moath = User('Moath', 'hello@axsos')
mohammad=User('mohammad','hi@hotmail.com')
Moath.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50)
mohammad.make_deposit(200).make_deposit(300).make_deposit(300).make_withdrawal(50)
print(mohammad.account_balance.display_account_info())
print(Moath.account_balance.display_account_info())