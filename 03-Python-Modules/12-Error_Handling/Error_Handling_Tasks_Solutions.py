"""
====================================================
ERROR HANDLING — try / except
TASK SOLUTIONS (RANK 1 → RANK 5)
====================================================

This file contains clean, professional solutions
for all Error Handling tasks.

Rules followed:
✔ Proper use of try / except
✔ Multiple exception handling
✔ Custom exceptions
✔ try / except / else / finally
✔ Professional formatting
"""

# ====================================================
# 🟢 RANK 1 — VERY EASY
# ====================================================

# Task 1 Solution
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


# Task 2 Solution
try:
    value = int("abc")
except ValueError:
    print("Error: Cannot convert string to integer")


# Task 3 Solution
numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range")


# ====================================================
# 🟡 RANK 2 — EASY
# ====================================================

# Task 4 Solution
try:
    age = int(input("Enter your age: "))
    print("Age recorded:", age)
except ValueError:
    print("Error: Age must be a number")


# Task 5 Solution
try:
    file = open("data.txt")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found")


# Task 6 Solution
user = {"name": "Peyman"}

try:
    print(user["age"])
except KeyError:
    print("Error: Key does not exist")


# ====================================================
# 🟠 RANK 3 — INTERMEDIATE
# ====================================================

# Task 7 Solution
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Error: Invalid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# Task 8 Solution
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Calculation failed")
else:
    print("Calculation successful:", result)


# Task 9 Solution
try:
    print("Processing...")
    value = int("123")
except ValueError:
    print("Error occurred")
finally:
    print("Process finished")


# ====================================================
# 🔵 RANK 4 — ADVANCED
# ====================================================

# Task 10 Solution
def check_password(password):
    if password != "admin123":
        raise Exception("Invalid password")

try:
    check_password("guest")
except Exception as e:
    print("Login failed:", e)


# Task 11 Solution
def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty")

try:
    validate_email("")
except ValueError as e:
    print("Validation error:", e)


# Task 12 Solution
try:
    result = 10 / 0
except Exception as e:
    print("Caught exception:", e)


# ====================================================
# 🔴 RANK 5 — PROFESSIONAL
# ====================================================

# Task 13 Solution
class InvalidLoginError(Exception):
    pass

def login(username, password):
    if username != "admin" or password != "1234":
        raise InvalidLoginError("Invalid login credentials")

try:
    login("user", "0000")
except InvalidLoginError as e:
    print("Login error:", e)


# Task 14 Solution
def process_payment(amount):
    if amount <= 0:
        raise ValueError("Payment amount must be positive")
    print("Payment processed:", amount)

try:
    process_payment(-50)
except ValueError as e:
    print("Payment error:", e)


# Task 15 Solution
class SystemError(Exception):
    pass

try:
    user_input = input("Enter system code: ")
    if user_input != "SYS2026":
        raise SystemError("Invalid system code")
except SystemError as e:
    print("System error:", e)
else:
    print("Access granted")
finally:
    print("System session ended")


# ====================================================
# END OF SOLUTIONS — ERROR HANDLING
# ====================================================

"""
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
"""
