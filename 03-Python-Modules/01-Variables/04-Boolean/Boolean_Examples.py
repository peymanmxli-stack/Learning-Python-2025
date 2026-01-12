"""
📂 Module — Basic Data Types: Boolean (bool)
📘 Examples File

This file contains focused, runnable examples that demonstrate how
Boolean values and logical expressions work in real Python code.

How to use this file:
- Run it with:  python Boolean_Examples.py
- Read the output carefully.
- Change values and observe how Boolean logic affects program behavior.
"""


# ===========================================================================
# 🔹 Example 1: Basic Boolean Values
# ===========================================================================
is_online = True
is_verified = False

print(is_online)
print(is_verified)
print(type(is_online))


# ===========================================================================
# 🔹 Example 2: Booleans from Comparisons
# ===========================================================================
x = 15
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x >= 10)


# ===========================================================================
# 🔹 Example 3: Logical Operators
# ===========================================================================
has_account = True
has_subscription = False

print(has_account and has_subscription)
print(has_account or has_subscription)
print(not has_subscription)


# ===========================================================================
# 🔹 Example 4: Booleans in if Statements
# ===========================================================================
age = 21

if age >= 18:
    print("User is an adult")
else:
    print("User is a minor")


# ===========================================================================
# 🔹 Example 5: Truthy and Falsy Values
# ===========================================================================
values = [0, 1, "", "Python", [], [1, 2, 3], None]

for value in values:
    print(value, "→", bool(value))


# ===========================================================================
# 🔹 Example 6: Combining Multiple Conditions
# ===========================================================================
username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Access granted")
else:
    print("Access denied")


# ===========================================================================
# 🔹 Example 7: Using or for Alternatives
# ===========================================================================
role = "editor"

if role == "admin" or role == "editor":
    print("User can edit content")
else:
    print("Read-only access")


# ===========================================================================
# 🔹 Example 8: not Operator
# ===========================================================================
is_banned = False

if not is_banned:
    print("User is allowed to login")


# ===========================================================================
# 🔹 Example 9: Boolean Variables for Readability
# ===========================================================================
is_logged_in = True
has_permission = True

if is_logged_in and has_permission:
    print("Action allowed")
else:
    print("Action denied")


# ===========================================================================
# 🔹 Example 10: Booleans in while Loops
# ===========================================================================
running = True
counter = 0

while running:
    print("Counter:", counter)
    counter += 1

    if counter == 3:
        running = False


# ===========================================================================
# 🔹 Example 11: Boolean Functions
# ===========================================================================
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))


# ===========================================================================
# 🔹 Example 12: Guard Clauses with Booleans
# ===========================================================================
def can_access(is_logged_in, is_admin):
    if not is_logged_in:
        return False
    if not is_admin:
        return False
    return True

print(can_access(True, True))
print(can_access(True, False))


# ===========================================================================
# 🔹 Example 13: Avoiding Common Mistakes
# ===========================================================================
x = 10

# ❌ Wrong (always True):
# if x == 10 or 20:

# ✔ Correct:
if x == 10 or x == 20:
    print("x is 10 or 20")


# ===========================================================================
# 🔹 Example 14: Clean Boolean Expressions
# ===========================================================================
temperature = 25

is_warm = temperature > 20
is_hot = temperature > 30

print("Warm:", is_warm)
print("Hot:", is_hot)


# ===========================================================================
# 🏁 End of Examples
# ===========================================================================


# 👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
