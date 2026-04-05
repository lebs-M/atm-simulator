# ATM / Banking Simulator CLI

A Python command-line ATM simulator that allows a user to check their balance, make deposits and withdrawals, and view a full transaction history. Account data is saved to a JSON file so it persists between sessions.

Built as part of my Software Engineering studies to practise object-oriented programming, file handling, input validation, and unit testing.

---

## Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Check Balance | View your current account balance |
| 2 | Withdraw | Withdraw funds with insufficient-funds protection |
| 3 | Deposit | Deposit funds into your account |
| 4 | Transaction History | View a timestamped history of all transactions |
| 0 | Exit | Exit the application safely |

---

## How to Run

Make sure you have Python 3 installed, then:

```bash
# Clone the repository
git clone https://github.com/lebs-M/pattern-generator.git

# Navigate into the project folder
cd atm-simulator

# Install dependencies
pip install -r requirements.txt

# Run the program
python main.py
```

---

## Example Output

```
  Connecting to Python Bank...
  Account loaded successfully...

==========================================
          WELCOME TO PYTHON BANK
==========================================
  1. Check Balance
  2. Withdraw
  3. Deposit
  4. Transaction History
  0. Exit
==========================================
  Select an option: 3
  Enter deposit amount: R500

  ✓ Successfully deposited R500.00.

  +---------------------------------+
  |  Current Balance: R    1,500.00  |
  +---------------------------------+
```

---

## Running Tests

```bash
py -m pytest
```

Or with Python directly:

```bash
python -m pytest
```

---

## Project Structure

```
atm-simulator/
│
├── account.py              # Core banking logic (balance, deposit, withdraw, history)
├── cli.py                  # Menu logic and user interaction
├── utils.py                # Input validation and display formatting
├── test_account.py         # Unit tests for all account operations
│
├── account.json            # Persistent account data (auto-created)
├── main.py                 # Entry point
├── __init__.py
├── requirements.txt
└── README.md
```

---

## What I Learned

- Object-oriented programming: designing an `Account` class with clear responsibilities
- File handling: reading and writing JSON to persist data between sessions
- Input validation: handling invalid user input gracefully
- Unit testing with pytest: testing deposits, withdrawals, edge cases, and file persistence
- Separation of concerns: keeping logic, UI, and utilities in separate modules

---

## Future Improvements

- Multiple accounts with PIN login
- Transfer funds between accounts
- Daily withdrawal limits
- Account statement export to PDF or CSV

---

## Author

**Lebogang Manamela**
Aspiring Junior Developer | Pretoria, Gauteng
https://github.com/lebs-M
www.linkedin.com/in/lebogang-manamela-a30684207

###########################################