"""
====================================================
TESTING & DEBUGGING — TASKS
====================================================

This file contains structured practice tasks
for Testing & Debugging in Python.

Focus:
✔ Identifying errors
✔ Debugging logic
✔ Improving reliability
✔ Writing testable code

Difficulty:
🟢 Rank 1 → 🔴 Rank 5
"""

# ====================================================
# 🟢 RANK 1 — VERY EASY
# ====================================================

"""
Task 1:
Fix the syntax error in the function below
so it prints "Hello World".
"""

# def say_hello()
#     print("Hello World")


"""
Task 2:
The function prints a value but does not return it.
Modify it so the result can be stored in a variable.
"""

def add_numbers(a, b):
    print(a + b)


# ====================================================
# 🟡 RANK 2 — EASY
# ====================================================

"""
Task 3:
The function below crashes when dividing by zero.
Add error handling to prevent the crash.
"""

def divide(a, b):
    return a / b


"""
Task 4:
Fix the logic error so the function
returns the correct average.
"""

def calculate_average(a, b):
    return a + b / 2


# ====================================================
# 🟠 RANK 3 — INTERMEDIATE
# ====================================================

"""
Task 5:
The function should return True if the number is even.
There is a logic bug. Find and fix it.
"""

def is_even(number):
    if number % 2 == 1:
        return True
    return False


"""
Task 6:
Add print debugging statements to track
how the total price is calculated.
"""

def calculate_total(price, quantity):
    total = price * quantity
    return total


# ====================================================
# 🔵 RANK 4 — ADVANCED
# ====================================================

"""
Task 7:
Use try/except to handle invalid input
when converting a value to an integer.
"""

def convert_to_int(value):
    return int(value)


"""
Task 8:
Add assertions to validate:
- quantity must be positive
- price must be greater than zero
"""

def calculate_invoice(price, quantity):
    return price * quantity


# ====================================================
# 🔴 RANK 5 — PROFESSIONAL
# ====================================================

"""
Task 9:
Refactor the function to:
✔ Handle edge cases
✔ Prevent runtime errors
✔ Return meaningful error messages
"""

def get_percentage(value, total):
    return (value / total) * 100


"""
Task 10:
Create a testable function that:
✔ Takes a list of numbers
✔ Returns the highest value
✔ Handles empty lists safely
✔ Is easy to debug
"""

# Write your function below


# ====================================================
# END OF TASKS — TESTING & DEBUGGING
# ====================================================


# ====================================================
# 👤 Author Information
# ====================================================

"""
👤 Author: Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 Student ID: 250161
"""
