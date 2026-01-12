"""
🔀 Control Flow — if / elif / else
📘 Professional Notes

The if / elif / else structure allows Python programs to make decisions.
It controls which block of code executes based on boolean conditions.

This file explains conditional logic clearly, with examples,
patterns, and best practices.
"""


# ===========================================================================
# 🧠 1. What Is Conditional Execution?
# ===========================================================================

# Conditional execution means that different code runs
# depending on whether a condition is True or False.

is_logged_in = True

if is_logged_in:
    print("User is logged in")
else:
    print("User is not logged in")


# ===========================================================================
# 🔹 2. Basic if Statement
# ===========================================================================

age = 17

if age >= 18:
    print("Access granted")


# ===========================================================================
# 🔀 3. if / else
# ===========================================================================

score = 65

if score >= 70:
    print("Passed")
else:
    print("Failed")


# ===========================================================================
# 🔁 4. if / elif / else
# ===========================================================================

grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")


# ===========================================================================
# 🔢 5. Comparison Operators
# ===========================================================================

x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# ===========================================================================
# 🔗 6. Logical Operators
# ===========================================================================

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

if age < 18 or not has_id:
    print("Entry denied")


# ===========================================================================
# 🧩 7. Nested Conditions
# ===========================================================================

balance = 500

if balance > 0:
    if balance >= 100:
        print("Sufficient balance")
    else:
        print("Low balance")
else:
    print("No balance")

# Nested if-statements are valid but should be used carefully.


# ===========================================================================
# 🧼 8. Avoiding Deep Nesting
# ===========================================================================

# Early return inside functions improves readability.

def check_access(age):
    if age < 18:
        return "Denied"
    return "Granted"

print(check_access(20))


# ===========================================================================
# ⚠️ 9. Truthy and Falsy Values
# ===========================================================================

# Falsy values include:
# False, None, 0, "", [], {}, ()

items = []

if items:
    print("Items exist")
else:
    print("Items list is empty")


# ===========================================================================
# ❌ 10. Common Mistakes
# ===========================================================================

# ❌ Using assignment instead of comparison
# if x = 5:   # SyntaxError

# ❌ Overusing else
# Sometimes only an if is needed.

number = -3
if number < 0:
    print("Negative number")


# ===========================================================================
# ✅ 11. Best Practices
# ===========================================================================

# ✔ Keep conditions readable
# ✔ Use meaningful variable names
# ✔ Avoid deeply nested conditions
# ✔ Prefer elif over nested if
# ✔ Use early returns in functions
# ✔ Write conditions that express intent


# ===========================================================================
# 🧠 12. Summary
# ===========================================================================

# In this section, I learned:
# - How conditional execution works
# - How to use if, elif, and else
# - How Python evaluates conditions
# - How to combine conditions logically
# - How to avoid common mistakes
# - How to write clean, readable decision logic


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
# ===========================================================================
