"""
====================================================
TESTING & DEBUGGING — EXAMPLES
====================================================

This file provides practical, real-world examples
demonstrating testing and debugging techniques
in Python.

Focus:
✔ Understanding errors
✔ Identifying bugs
✔ Applying debugging methods
✔ Writing reliable code
"""

# ====================================================
# 1️⃣ SYNTAX ERROR EXAMPLES
# ====================================================

"""
Syntax errors prevent code from running.
They are detected before execution.
"""

# ❌ Example (Incorrect)
# if x == 5
#     print("Hello")

# ✅ Corrected Version
x = 5
if x == 5:
    print("Hello")


# ====================================================
# 2️⃣ RUNTIME ERROR (EXCEPTION) EXAMPLES
# ====================================================

"""
Runtime errors occur while the program is running.
"""

# ❌ Example: ZeroDivisionError
def divide_numbers(a, b):
    return a / b

# Uncommenting the line below will crash the program
# divide_numbers(10, 0)

# ✅ Safe Version
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# ====================================================
# 3️⃣ LOGIC ERROR EXAMPLES
# ====================================================

"""
Logic errors produce incorrect results
without crashing the program.
"""

# ❌ Incorrect Logic
def calculate_discount(price):
    return price - 10  # Wrong for percentages

# ✅ Correct Logic
def calculate_discount(price):
    return price * 0.90


# ====================================================
# 4️⃣ PRINT DEBUGGING
# ====================================================

"""
Using print() to inspect values and execution flow.
"""

def calculate_total(price, quantity):
    print("Price:", price)
    print("Quantity:", quantity)
    total = price * quantity
    print("Total:", total)
    return total

calculate_total(10, 3)


# ====================================================
# 5️⃣ STEP-BY-STEP DEBUGGING
# ====================================================

"""
Breaking logic into steps helps isolate errors.
"""

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

print(calculate_average([10, 20, 30]))


# ====================================================
# 6️⃣ USING ASSERTIONS
# ====================================================

"""
Assertions validate assumptions during execution.
"""

def withdraw(balance, amount):
    assert amount >= 0, "Amount must be positive"
    assert amount <= balance, "Insufficient funds"
    return balance - amount

print(withdraw(1000, 200))


# ====================================================
# 7️⃣ SIMPLE MANUAL TESTING
# ====================================================

"""
Manually testing function outputs.
"""

def add(a, b):
    return a + b

print(add(2, 3))     # Expected: 5
print(add(-1, 1))    # Expected: 0
print(add(0, 0))     # Expected: 0


# ====================================================
# 8️⃣ TESTING EDGE CASES
# ====================================================

"""
Edge cases are unusual or extreme inputs.
"""

def get_first_item(items):
    if not items:
        return None
    return items[0]

print(get_first_item([1, 2, 3]))
print(get_first_item([]))  # Edge case


# ====================================================
# 9️⃣ DEBUGGING WITH TRY / EXCEPT
# ====================================================

"""
Handling errors gracefully instead of crashing.
"""

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return "Invalid number"

print(convert_to_int("123"))
print(convert_to_int("abc"))


# ====================================================
# 🔟 TESTING FUNCTION COMPOSITION
# ====================================================

"""
Testing functions that rely on other functions.
"""

def square(x):
    return x * x

def cube(x):
    return square(x) * x

print(cube(3))  # Expected: 27


# ====================================================
# 1️⃣1️⃣ DEBUGGING WRONG ASSUMPTIONS
# ====================================================

"""
Testing assumptions prevents hidden bugs.
"""

def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))


# ====================================================
# 1️⃣2️⃣ CLEAN & TESTABLE CODE EXAMPLE
# ====================================================

"""
Small, focused, predictable functions
are easier to test and debug.
"""

def calculate_tax(amount, rate):
    return amount * rate

print(calculate_tax(100, 0.15))


# ====================================================
# END OF EXAMPLES — TESTING & DEBUGGING
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
