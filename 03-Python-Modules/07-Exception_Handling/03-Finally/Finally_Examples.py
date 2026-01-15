"""
Finally_Examples.py

Topic: Exception Handling — finally

This file contains runnable examples that demonstrate how `finally`
controls program flow in different situations.

How to use this file:
- Run it with: python Finally_Examples.py
- Read the comments before each example
- Observe the output carefully
"""

# ==================================================
# Example 1 — finally always runs (no error)
# ==================================================
print("\nExample 1 — No error")
try:
    print("Inside try block")
finally:
    print("Inside finally block")


# ==================================================
# Example 2 — finally runs even when an error occurs
# ==================================================
print("\nExample 2 — Error occurs")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Caught division by zero")
finally:
    print("Cleanup executed")


# ==================================================
# Example 3 — finally runs even if exception is not handled
# ==================================================
print("\nExample 3 — Unhandled exception")
try:
    x = int("abc")
finally:
    print("Finally runs before crash")

# NOTE:
# Program will stop here due to ValueError
# The code below will NOT execute


# ==================================================
# Example 4 — finally with return
# ==================================================
print("\nExample 4 — finally with return")

def example_return():
    try:
        return "Returned from try"
    finally:
        print("Finally executed before return")

print(example_return())


# ==================================================
# Example 5 — finally inside a loop with break
# ==================================================
print("\nExample 5 — finally with break")
for i in range(3):
    try:
        print("Loop iteration:", i)
        if i == 1:
            break
    finally:
        print("Finally runs at iteration", i)


# ==================================================
# Example 6 — finally inside a loop with continue
# ==================================================
print("\nExample 6 — finally with continue")
for i in range(3):
    try:
        if i == 1:
            continue
        print("Processing:", i)
    finally:
        print("Finally runs at iteration", i)


# ==================================================
# Example 7 — finally used for file handling
# ==================================================
print("\nExample 7 — File handling with finally")

file = None
try:
    file = open("sample.txt", "w")
    file.write("Learning finally in Python")
    print("File written successfully")
finally:
    if file:
        file.close()
        print("File closed safely")


# ==================================================
# Example 8 — finally vs with (conceptual comparison)
# ==================================================
print("\nExample 8 — finally vs with")

# Using finally
f = open("sample2.txt", "w")
try:
    f.write("Using finally")
finally:
    f.close()

# Using with (recommended)
with open("sample3.txt", "w") as f:
    f.write("Using with")

print("Both files written and closed")


# ==================================================
# End of Finally_Examples.py
# ==================================================
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
