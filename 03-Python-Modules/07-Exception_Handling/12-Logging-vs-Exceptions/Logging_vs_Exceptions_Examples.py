import logging

logging.basicConfig(level=logging.INFO)

# Example 1: Logging without exception
def load_config(file):
    logging.info("Loading configuration file")
    if not file:
        logging.warning("Config file name is empty")
        return None
    return "Config loaded"

# Example 2: Exception without logging
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

# Example 3: Logging + Exception
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        logging.error(f"File not found: {filename}")
        raise

# Example 4: Do NOT swallow exceptions
try:
    divide(10, 0)
except ZeroDivisionError:
    logging.critical("Fatal calculation error")
    raise
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
