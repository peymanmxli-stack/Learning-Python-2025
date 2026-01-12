"""
🚨 Exception Handling — try Statement
Professional Notes

The try statement is used to wrap code that may raise runtime errors.
It allows Python to attempt execution safely without crashing immediately.
"""


# ===========================================================================
# 🔹 1. What Is try?
# ===========================================================================
# The try block tells Python:
# "Attempt to run this code. If something goes wrong, handle it later."

# Example (will crash without try):
# result = 10 / 0


# ===========================================================================
# 🔹 2. Basic try Structure
# ===========================================================================
# try:
#     risky code
# except:
#     error handling

try:
    result = 10 / 2
    print(result)
except:
    print("An error occurred")


# ===========================================================================
# 🔹 3. Why Use try?
# ===========================================================================
# Some operations are unpredictable:
# - User input
# - File access
# - Type conversion
# - Mathematical operations

try:
    value = int("abc")
except:
    print("Conversion failed")


# ===========================================================================
# 🔹 4. try Only Marks Risky Code
# ===========================================================================
# The try block DOES NOT fix errors.
# It only prevents crashes and redirects flow.

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except:
    print("Index error detected")


# ===========================================================================
# 🔹 5. Scope of try
# ===========================================================================
# Only code inside the try block is monitored.

try:
    x = 5
    y = 0
    z = x / y
    print("This line will not run")
except:
    print("Error occurred inside try")


# ===========================================================================
# 🔹 6. What Should Go Inside try?
# ===========================================================================
# ✔ Code that may realistically fail
# ❌ Entire programs
# ❌ Logic that should not fail

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("Number:", number)
except:
    print("Invalid input")


# ===========================================================================
# 🔹 7. Common Errors Triggered Inside try
# ===========================================================================
# ZeroDivisionError
# ValueError
# TypeError
# IndexError
# FileNotFoundError


# ===========================================================================
# 🔹 8. try Without except (Not Useful Alone)
# ===========================================================================
# A try block must be followed by except, else, or finally.
# try alone is invalid syntax.


# ===========================================================================
# 🔹 9. Best Practices
# ===========================================================================
# ✔ Keep try blocks minimal
# ✔ Place only risky statements inside
# ✔ Avoid generic except (learned later)
# ✔ Prepare for specific exception handling


# ===========================================================================
# 🧠 Summary
# ===========================================================================
# In this module, I learned:
# - The purpose of the try statement
# - How try protects risky code
# - When to use try
# - What happens when errors occur
# - Why try is the foundation of exception handling


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
