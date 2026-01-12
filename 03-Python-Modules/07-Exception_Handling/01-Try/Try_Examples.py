"""
🚨 Exception Handling — try Statement
Examples File

This file demonstrates how the try block is used to protect risky code.
Error handling logic will be expanded later using except, else, and finally.
"""


# ===========================================================================
# 🟢 Example 1 — try with safe execution
# ===========================================================================

try:
    result = 10 + 5
    print("Result:", result)
except:
    print("An error occurred")



# ===========================================================================
# 🟢 Example 2 — Protecting division
# ===========================================================================

try:
    result = 10 / 2
    print("Division result:", result)
except:
    print("Division failed")



# ===========================================================================
# 🟢 Example 3 — Type conversion risk
# ===========================================================================

try:
    number = int("42")
    print("Converted number:", number)
except:
    print("Conversion failed")



# ===========================================================================
# 🟡 Example 4 — User input protection
# ===========================================================================

try:
    user_input = input("Enter a number: ")
    value = int(user_input)
    print("You entered:", value)
except:
    print("Invalid input")



# ===========================================================================
# 🟡 Example 5 — List index access
# ===========================================================================

items = [10, 20, 30]

try:
    print(items[1])
except:
    print("Index error")



# ===========================================================================
# 🟠 Example 6 — Multiple risky operations
# ===========================================================================

try:
    x = int("5")
    y = int("0")
    print(x / y)
except:
    print("An error occurred during calculation")



# ===========================================================================
# 🟠 Example 7 — File opening attempt
# ===========================================================================

try:
    file = open("sample.txt", "r")
    print(file.read())
except:
    print("File operation failed")



# ===========================================================================
# 🔴 Example 8 — Loop with try
# ===========================================================================

values = ["10", "x", "5"]

for v in values:
    try:
        print(int(v))
    except:
        print("Conversion error")



# ===========================================================================
# 🟣 Example 9 — Function execution safety
# ===========================================================================

def multiply(a, b):
    return a * b

try:
    print(multiply(4, 3))
except:
    print("Function failed")



# ===========================================================================
# 🧠 Example 10 — Demonstrating try scope
# ===========================================================================

try:
    print("Inside try block")
    result = 5 / 0
    print("This will not run")
except:
    print("Error detected inside try block")



# ===========================================================================
# 🧠 End of Examples
# ===========================================================================
# Concepts demonstrated:
# - Using try to protect risky code
# - Preventing crashes
# - Scope of try blocks
# - Preparing for proper exception handling
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
