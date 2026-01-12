"""
🚨 Exception Handling — except Statement
Professional Notes

The except block defines how Python responds when an error occurs
inside a try block. It is responsible for handling runtime exceptions.
"""


# ===========================================================================
# 🔹 1. What Is except?
# ===========================================================================
# The except block runs ONLY if an exception occurs in try.

try:
    result = 10 / 0
except:
    print("An error occurred")


# ===========================================================================
# 🔹 2. Generic except (Educational Only)
# ===========================================================================
# Catches all exceptions.
# Useful for learning, but not recommended for production.

try:
    value = int("abc")
except:
    print("Conversion failed")


# ===========================================================================
# 🔹 3. Catching Specific Exceptions
# ===========================================================================
# This is the professional and recommended approach.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# ===========================================================================
# 🔹 4. Handling Different Errors Separately
# ===========================================================================

try:
    value = int(None)
except ValueError:
    print("Value error occurred")
except TypeError:
    print("Type error occurred")


# ===========================================================================
# 🔹 5. Catching Multiple Exceptions Together
# ===========================================================================
# Useful when handling logic is the same.

try:
    number = int("x")
except (ValueError, TypeError):
    print("Conversion error")


# ===========================================================================
# 🔹 6. Capturing the Error Object
# ===========================================================================
# Allows access to the error message.

try:
    result = 5 / 0
except ZeroDivisionError as error:
    print("Error message:", error)


# ===========================================================================
# 🔹 7. except Controls Program Flow
# ===========================================================================
# Code after except continues execution normally.

try:
    items = [1, 2, 3]
    print(items[10])
except IndexError:
    print("Invalid index")

print("Program continues running")


# ===========================================================================
# 🔹 8. What except Should Handle
# ===========================================================================
# ✔ Predictable runtime errors
# ✔ User input mistakes
# ✔ File access issues
# ❌ Logic errors
# ❌ Programming bugs


# ===========================================================================
# 🔹 9. except Order Matters
# ===========================================================================
# Specific exceptions must come BEFORE generic ones.

try:
    x = int("abc")
except ValueError:
    print("Value error")
except Exception:
    print("Generic error")


# ===========================================================================
# 🔹 10. Best Practices
# ===========================================================================
# ✔ Catch specific exceptions
# ✔ Avoid swallowing errors silently
# ✔ Keep error handling readable
# ✔ Log or report errors when appropriate


# ===========================================================================
# 🧠 Summary
# ===========================================================================
# In this module, I learned:
# - The role of the except block
# - How to catch specific exceptions
# - Why generic except is risky
# - How except affects program flow
# - Professional exception handling patterns


# ===========================================================================
# 👤 Author
# ===========================================================================
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
# 🏁 End of Notes
