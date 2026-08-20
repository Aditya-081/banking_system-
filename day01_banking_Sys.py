import json
import os

FILE = "accounts.json"


def load_accounts():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return {}


def save_accounts(accounts):
    with open(FILE, "w") as file:
        json.dump(accounts, file, indent=4)


def create_account(accounts):
    print("\n===== CREATE ACCOUNT =====")

    name = input("Enter your name: ")
    pin = input("Create a 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    account_number = str(100000 + len(accounts) + 1)

    accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    save_accounts(accounts)

    print("\nAccount created successfully!")
    print("Your account number:", account_number)


def main():
    accounts = load_accounts()

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            print("Thank you for using our banking system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()