import logging

logging.basicConfig(level=logging.INFO)

# Rank 1
def start_app():
    logging.info("Application started")

# Rank 2
def check_age(age):
    if age < 0:
        logging.warning("Negative age provided")
        return False
    return True

# Rank 3
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

# Rank 4
def open_file(name):
    try:
        with open(name):
            logging.info("File opened successfully")
    except FileNotFoundError:
        logging.error("File does not exist")
        raise

# Rank 5
def process_payment(amount):
    logging.info("Processing payment")
    if amount <= 0:
        logging.error("Invalid payment amount")
        raise ValueError("Amount must be positive")
    logging.info("Payment successful")

👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
