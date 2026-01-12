"""
🚨 Exception Handling — Examples

This file contains practical, runnable examples demonstrating how Python
handles runtime errors using try / except / else / finally and raise.

Run this file and read each section carefully.
Modify values to observe different behaviors.
"""


# ===========================================================================
# 🟢 Example 1 — Basic try / except
# ===========================================================================

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


# ===========================================================================
# 🟢 Example 2 — Handling ValueError
# ===========================================================================

user_input = "abc"

try:
    number = int(user_input)
except ValueError:
    print("Error: Cannot convert input to integer")


# ===========================================================================
# 🟢 Example 3 — Multiple except blocks
# ===========================================================================

data = None

try:
    value = int(data)
except ValueError:
    print("ValueError: Invalid value")
except TypeError:
    print("TypeError: Wrong data type")


# ===========================================================================
# 🟢 Example 4 — Catching multiple exceptions together
# ===========================================================================

try:
    result = 10 / int("x")
except (ZeroDivisionError, ValueError):
    print("Error: Invalid mathematical operation")


# ===========================================================================
# 🟡 Example 5 — Using else
# ===========================================================================

try:
    number = int("42")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", number)


# ===========================================================================
# 🟡 Example 6 — Using finally
# ===========================================================================

try:
    file = open("example.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File does not exist")
finally:
    print("Execution completed (cleanup can happen here)")


# ===========================================================================
# 🟡 Example 7 — Generic exception (educational only)
# ===========================================================================

try:
    items = [1, 2, 3]
    print(items[10])
except Exception as error:
    print("Caught error:", error)


# ===========================================================================
# 🟠 Example 8 — Raising an exception manually
# ===========================================================================

age = -3

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as error:
    print("Validation error:", error)


# ===========================================================================
# 🟠 Example 9 — Function with validation
# ===========================================================================

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as error:
    print("Function error:", error)


# ===========================================================================
# 🔴 Example 10 — Input validation loop
# ===========================================================================

while True:
    try:
        value = int(input("Enter a number (0 to exit): "))
        if value == 0:
            break
        print("You entered:", value)
    except ValueError:
        print("Invalid input, please enter a number")


# ===========================================================================
# 🟣 Example 11 — Realistic file handling pattern
# ===========================================================================

filename = "data.txt"

try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: '{filename}' not found")
except PermissionError:
    print("Error: Permission denied")
else:
    print("File read successfully")
finally:
    print("File operation finished")


# ===========================================================================
# 🧠 End of Examples
# ===========================================================================
# Concepts demonstrated:
# - try / except basics
# - multiple exception handling
# - else and finally blocks
# - manual exception raising
# - validation and defensive programming
