"""
🚨 Exception Handling — except Statement
Examples File

This file demonstrates how the except block handles errors
raised inside try blocks.
"""


# ===========================================================================
# 🟢 Example 1 — Generic except (basic behavior)
# ===========================================================================

try:
    result = 10 / 0
except:
    print("An error occurred")



# ===========================================================================
# 🟢 Example 2 — Catching ZeroDivisionError
# ===========================================================================

try:
    value = 20 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")



# ===========================================================================
# 🟢 Example 3 — Catching ValueError
# ===========================================================================

try:
    number = int("abc")
except ValueError:
    print("Invalid integer conversion")



# ===========================================================================
# 🟡 Example 4 — Multiple except blocks
# ===========================================================================

try:
    value = int(None)
except ValueError:
    print("ValueError occurred")
except TypeError:
    print("TypeError occurred")



# ===========================================================================
# 🟡 Example 5 — Catching multiple exceptions together
# ===========================================================================

try:
    number = int("x")
except (ValueError, TypeError):
    print("Conversion error")



# ===========================================================================
# 🟠 Example 6 — Capturing exception details
# ===========================================================================

try:
    result = 5 / 0
except ZeroDivisionError as error:
    print("Error message:", error)



# ===========================================================================
# 🟠 Example 7 — except and program flow
# ===========================================================================

try:
    items = [1, 2, 3]
    print(items[10])
except IndexError:
    print("Index out of range")

print("Program continues normally")



# ===========================================================================
# 🔴 Example 8 — except order matters
# ===========================================================================

try:
    value = int("abc")
except ValueError:
    print("ValueError caught")
except Exception:
    print("Generic exception caught")



# ===========================================================================
# 🔴 Example 9 — Handling file errors
# ===========================================================================

try:
    file = open("missing.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")



# ===========================================================================
# 🟣 Example 10 — except inside loop
# ===========================================================================

values = ["10", "x", None, "5"]

for v in values:
    try:
        print(int(v))
    except (ValueError, TypeError):
        print("Invalid value")



# ===========================================================================
# 🧠 End of Examples
# ===========================================================================
# Concepts demonstrated:
# - Generic vs specific except
# - Multiple except blocks
# - Capturing exception objects
# - except ordering
# - Error handling inside loops
# ===========================================================================
# 👤 Author
# ===========================================================================
👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
🏁 End of Examples
