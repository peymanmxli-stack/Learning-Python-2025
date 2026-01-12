"""
🔀 Control Flow — if / elif / else
📂 Examples File

This file contains focused, runnable examples demonstrating how
if / elif / else statements work in real Python programs.

How to use this file:
- Run it with:  python If_Elif_Else_Examples.py
- Change values to observe different execution paths
"""


# ===========================================================================
# Example 1 — Simple if
# ===========================================================================
age = 20

if age >= 18:
    print("Adult")


# ===========================================================================
# Example 2 — if / else
# ===========================================================================
score = 60

if score >= 70:
    print("Passed")
else:
    print("Failed")


# ===========================================================================
# Example 3 — if / elif / else
# ===========================================================================
grade = 82

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# ===========================================================================
# Example 4 — Using Logical Operators
# ===========================================================================
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
else:
    print("Entry denied")


# ===========================================================================
# Example 5 — Multiple Conditions with or
# ===========================================================================
is_admin = False
is_editor = True

if is_admin or is_editor:
    print("Access granted")
else:
    print("Access denied")


# ===========================================================================
# Example 6 — Nested if Statements
# ===========================================================================
balance = 150

if balance > 0:
    if balance >= 100:
        print("Sufficient balance")
    else:
        print("Low balance")
else:
    print("No balance")


# ===========================================================================
# Example 7 — Early Return in Functions
# ===========================================================================
def check_access(age):
    if age < 18:
        return "Denied"
    return "Granted"

print(check_access(16))
print(check_access(22))


# ===========================================================================
# Example 8 — Truthy and Falsy Values
# ===========================================================================
items = []

if items:
    print("Items found")
else:
    print("No items found")


# ===========================================================================
# Example 9 — Condition Without else
# ===========================================================================
temperature = -5

if temperature < 0:
    print("Freezing temperature")


# ===========================================================================
# Example 10 — Readable Conditions
# ===========================================================================
username = "admin"
password_correct = True

if username == "admin" and password_correct:
    print("Login successful")
else:
    print("Login failed")


# ===========================================================================
# 👤 Author
# ===========================================================================
👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161

# 🏁 End of Examples
# ===========================================================================
