# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if there are sufficient funds."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True

