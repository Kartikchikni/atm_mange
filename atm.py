class BankAccount:

    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print("Deposit Successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def change_pin(self):
        old_pin = int(input("Enter Current PIN: "))

        if old_pin == self.pin:
            new_pin = int(input("Enter New PIN: "))
            confirm_pin = int(input("Confirm New PIN: "))

            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN Changed Successfully")
            else:
                print("PINs Do Not Match")
        else:
            print("Wrong PIN")

    def show_history(self):
        if len(self.transactions) == 0:
            print("No Transactions Found")
        else:
            print("\n===== Transaction History =====")
            for i, transaction in enumerate(self.transactions, start=1):
                print(f"{i}. {transaction}")


# Multiple Accounts
accounts = {
    14092006: BankAccount(14092006, 1960, 50000),
    14092007: BankAccount(14092007, 1234, 25000),
    14092008: BankAccount(14092008, 5678, 10000)
}


# Login
acc_num = int(input("Enter Account Number: "))
atm_pin = int(input("Enter PIN: "))

if acc_num in accounts and accounts[acc_num].pin == atm_pin:

    user = accounts[acc_num]

    print("Login Successful")

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            user.check_balance()

        elif choice == 2:
            amount = int(input("Enter Deposit Amount: "))
            user.deposit(amount)

        elif choice == 3:
            amount = int(input("Enter Withdraw Amount: "))
            user.withdraw(amount)

        elif choice == 4:
            user.change_pin()

        elif choice == 5:
            user.show_history()

        elif choice == 6:
            print("Thank You For Using ATM")
            break

        else:
            print("Invalid Choice")

else:
    print("Invalid Account Number or PIN")