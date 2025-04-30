class ATM:
    def __init__(self, balance=1000, pin="1234"):
        self.balance = balance
        self.pin = pin

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("\nAuthentication successful.\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. {attempts} attempt(s) left.")
        print("\nToo many incorrect attempts. Exiting.")
        return False

    def display_menu(self):
        print("--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        print(f"\nYour current balance is ₹{self.balance}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} deposited successfully.")
                self.check_balance()
            else:
                print("Invalid amount. Deposit cancelled.")
        except ValueError:
            print("Invalid input. Deposit cancelled.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"₹{amount} withdrawn successfully.")
                    self.check_balance()
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid amount. Withdrawal cancelled.")
        except ValueError:
            print("Invalid input. Withdrawal cancelled.")

    def run(self):
        if not self.authenticate():
            return

        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the ATM simulator
if __name__ == "__main__":
    atm = ATM()
    atm.run()
