class BankAccount:
    def __init__(self, account_balance=0,):
        self.balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display_balance(self):
        return print(f"Current Balance: ${self.balance:.2f}")