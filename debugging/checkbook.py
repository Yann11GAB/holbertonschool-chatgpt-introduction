class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Ajoute un montant au solde."""
        if amount < 0:
            print("Amount cannot be negative. Please try again.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """Retire un montant du solde, si suffisant."""
        if amount < 0:
            print("Amount cannot be negative. Please try again.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """Affiche le solde actuel."""
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, "
                       "balance, exit): ").strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
