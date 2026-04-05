def get_amount(prompt="Enter amount"):
    """Prompt the user for a valid positive monetary amount."""
    while True:
        try:
            value = float(input(f"{prompt}: R"))
            if value <= 0:
                print("  Amount must be greater than zero.")
            else:
                return round(value, 2)
        except ValueError:
            print("  Invalid input. Please enter a number (e.g. 500 or 150.50).")


def display_menu():
    """Print the ATM main menu."""
    print("\n" + "=" * 42)
    print("          WELCOME TO PYTHON BANK")
    print("=" * 42)
    print("  1. Check Balance")
    print("  2. Withdraw")
    print("  3. Deposit")
    print("  4. Transaction History")
    print("  0. Exit")
    print("=" * 42)


def display_balance(balance):
    """Display the current account balance."""
    print("\n  +---------------------------------+")
    print(f"  |  Current Balance: R{balance:>12,.2f}  |")
    print("  +---------------------------------+")


def display_history(transactions):
    """Display a formatted transaction history."""
    print("\n" + "-" * 42)
    print("        TRANSACTION HISTORY")
    print("-" * 42)

    if not transactions:
        print("  No transactions yet.")
    else:
        for t in transactions:
            symbol = "+" if t["type"] == "DEPOSIT" else "-"
            print(f"  {t['date']}  |  {t['type']:<12}  |  {symbol}R{t['amount']:>10,.2f}")

    print("-" * 42)
