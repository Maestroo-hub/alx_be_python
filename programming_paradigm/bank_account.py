import sys


class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes the bank account with an optional initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposits a specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account, if sufficient funds are available."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Displays the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")

from bank_account import BankAccount


def main():
    account = BankAccount(100)  # Start with an example balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()


