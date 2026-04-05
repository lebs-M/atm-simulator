from account import Account
from utils import display_menu, display_balance, display_history, get_amount


def run(): # start the application
    account = Account()

    print("\n  Connecting to Python Bank...")
    print("  Account loaded successfully...")

    while True:
        display_menu()
        choice = input("  Select an option: ").strip()

        if choice == "0":
            print("\n  Thank you for banking with Python Bank.")
            print("  Goodbye...\n")
            break

        elif choice == "1":
            display_balance(account.get_balance())

        elif choice == "2":
            display_balance(account.get_balance())
            amount = get_amount("  Enter withdrawal amount")
            success, message = account.withdraw(amount)
            print(f"\n  {'✓' if success else 'x'} {message}") 
            if success:
                display_balance(account.get_balance())

        elif choice == "3":
            amount = get_amount("  Enter deposit amount")
            success, message = account.deposit(amount)
            print(f"\n  {'✓' if success else 'x'} {message}")
            if success:
                display_balance(account.get_balance())

        elif choice == "4":
            display_history(account.get_history())

        else:
            print("\n  Invalid option. Please choose from the menu.")
