"""
🚨 Exception Handling — Professional Notes

Exceptions are runtime errors that interrupt the normal flow of a program.
Python provides a structured way to detect and handle these errors gracefully.
"""


# ===========================================================================
# 🔹 1. What Is an Exception?
# ===========================================================================
# An exception is an event that occurs during execution and disrupts normal flow.

# Example:
# print(10 / 0)  → ZeroDivisionError


# ===========================================================================
# 🔹 2. Basic try / except
# ===========================================================================
# Used to catch and handle errors safely.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero")


# ===========================================================================
# 🔹 3. Handling Multiple Exceptions
# ===========================================================================

try:
    number = int("abc")
except ValueError:
    print("Invalid number format")
except TypeError:
    print("Wrong type used")


# ===========================================================================
# 🔹 4. Catching Multiple Exceptions Together
# ===========================================================================

try:
    value = int(None)
except (ValueError, TypeError):
    print("Conversion failed")


# ===========================================================================
# 🔹 5. Generic Exception (Use Carefully)
# ===========================================================================
# Not recommended unless absolutely necessary.

try:
    x = 5 / 0
except Exception as error:
    print("Error occurred:", error)


# ===========================================================================
# 🔹 6. The else Block
# ===========================================================================
# Executes only if NO exception occurs.

try:
    value = int("42")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful:", value)


# ===========================================================================
# 🔹 7. The finally Block
# ===========================================================================
# Always executes, with or without errors.

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing resources if needed")


# ===========================================================================
# 🔹 8. Raising Exceptions
# ===========================================================================
# Used to signal errors intentionally.

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")


# ===========================================================================
# 🔹 9. Custom Error Messages
# ===========================================================================

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


# ===========================================================================
# 🔹 10. Common Built-in Exceptions
# ===========================================================================
# ValueError        → invalid value
# TypeError         → wrong data type
# ZeroDivisionError → division by zero
# IndexError        → invalid index
# KeyError          → missing dictionary key
# FileNotFoundError → missing file


# ===========================================================================
# 🔹 11. Best Practices
# ===========================================================================
# ✔ Catch specific exceptions
# ✔ Avoid bare except:
# ✔ Use finally for cleanup
# ✔ Never ignore exceptions silently
# ✔ Use raise for validation logic


# ===========================================================================
# 🧠 Summary
# ===========================================================================
# In this module, I learned:
# - What exceptions are and why they happen
# - How to use try / except blocks
# - How to handle multiple exceptions
# - The purpose of else and finally
# - How and when to raise exceptions
# - Writing safer and more professional Python code


# ===========================================================================
# 👤 Author
# ===========================================================================
👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
# 🏁 End of Notes
