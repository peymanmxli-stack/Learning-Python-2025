"""
📘 Module — Basic Data Types: Boolean (bool)
Professional Notes

Booleans represent truth values in Python. They are the foundation of
decision-making in programs and control how code behaves.

Booleans are used in conditions, comparisons, validations, permissions,
loops, and logic that determines which code runs and which does not.

Understanding Boolean logic is essential for writing correct, readable,
and professional Python programs.
"""


# ===========================================================================
# 🧵 1. What Is a Boolean?
# ===========================================================================
# A Boolean (bool) represents one of two values:
#   - True
#   - False
#
# Booleans are used to represent truth and falsity.

is_active = True
is_admin = False

print(is_active)
print(is_admin)
print(type(is_active))


# ===========================================================================
# 🔢 2. Creating Booleans with Comparisons
# ===========================================================================
# Most Booleans come from comparisons.

a = 10
b = 20

print(a == b)   # equal
print(a != b)   # not equal
print(a < b)    # less than
print(a > b)    # greater than
print(a <= 10)  # less than or equal
print(b >= 15)  # greater than or equal


# ===========================================================================
# 🧮 3. Logical Operators (and, or, not)
# ===========================================================================
# Logical operators combine or modify Boolean values.

x = True
y = False

print(x and y)  # True if both are True
print(x or y)   # True if at least one is True
print(not x)    # Inverts the Boolean value


# ===========================================================================
# 🔀 4. Booleans in Conditional Statements
# ===========================================================================
# Booleans control program flow using if / elif / else.

age = 18

if age >= 18:
    print("Access granted")
else:
    print("Access denied")


# ===========================================================================
# ⚖️ 5. Truthy and Falsy Values
# ===========================================================================
# Not all values are True or False, but Python evaluates them as such.

# Falsy values:
#   False, 0, 0.0, "", [], {}, None

print(bool(0))
print(bool(""))
print(bool([]))

# Truthy values:
print(bool(1))
print(bool("Python"))
print(bool([1, 2, 3]))


# ===========================================================================
# 🔍 6. Boolean Expressions in Practice
# ===========================================================================
# Real programs often use multiple conditions together.

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# ===========================================================================
# 🛑 7. Common Logical Mistakes
# ===========================================================================
# ❌ Incorrect comparison chaining:
# if x == 10 or 20:   → always True
#
# ✔ Correct way:
x = 10
if x == 10 or x == 20:
    print("x is 10 or 20")


# ===========================================================================
# 🧼 8. Clean and Readable Boolean Logic
# ===========================================================================
# Use meaningful variable names for clarity.

is_logged_in = True
has_permission = False

if is_logged_in and has_permission:
    print("Action allowed")
else:
    print("Action denied")


# ===========================================================================
# 🔁 9. Booleans in Loops
# ===========================================================================
# Booleans often control when loops stop.

running = True
counter = 0

while running:
    print("Counter:", counter)
    counter += 1
    if counter == 3:
        running = False


# ===========================================================================
# ⚡ 10. Boolean Functions
# ===========================================================================
# Functions often return Boolean values.

def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))


# ===========================================================================
# ✅ 11. Best Practices
# ===========================================================================
# ✔ Write clear Boolean expressions
# ✔ Use meaningful variable names (is_, has_, can_)
# ✔ Avoid overly complex conditions
# ✔ Prefer readability over clever logic
# ✔ Use parentheses when logic becomes complex
# ✔ Test Boolean logic carefully


# ===========================================================================
# 🧠 12. Summary
# ===========================================================================
# In this module, I learned:
# - What Boolean values are and how they work
# - How comparisons produce Boolean results
# - How to combine logic with and, or, and not
# - How Booleans control program flow
# - What truthy and falsy values mean
# - How to write clean, readable conditional logic
# - Best practices for professional Boolean usage
# ===========================================================================


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
