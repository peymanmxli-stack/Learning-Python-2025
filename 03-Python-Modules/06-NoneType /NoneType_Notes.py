"""
⭕ Module — NoneType (None)
📘 Professional Notes

In Python, None represents the absence of a value.
It is a real object with its own type: NoneType.

None is commonly used to indicate:
- no result
- no value yet
- optional data
- default or placeholder values
"""


# ===========================================================================
# 🔍 1. What Is None?
# ===========================================================================
# None is a special constant in Python.
# It means "nothing", "no value", or "empty reference".
# None is NOT:
# - 0
# - False
# - ""
# - an empty list

x = None
print(x)


# ===========================================================================
# 🧬 2. NoneType
# ===========================================================================
# None has a unique type: NoneType.

print(type(None))
print(type(x))


# ===========================================================================
# 🧠 3. Why None Exists
# ===========================================================================
# None is used when:
# - a variable has no meaningful value yet
# - a function does not return anything explicitly
# - an operation fails or finds nothing
# - a default value is required


# ===========================================================================
# 🔁 4. None and Functions
# ===========================================================================
# Functions return None by default if no return statement is used.

def say_hello():
    print("Hello")

result = say_hello()
print(result)  # None


# ===========================================================================
# ❓ 5. Checking for None (Correct Way)
# ===========================================================================
# Always use 'is' or 'is not' when comparing with None.

value = None

print(value is None)
print(value is not None)


# ===========================================================================
# ❌ 6. Incorrect Comparisons
# ===========================================================================
# Avoid using == or != with None.

# ❌ value == None
# ❌ value != None


# ===========================================================================
# 🧪 7. None in Conditional Statements
# ===========================================================================
# None is treated as False in boolean contexts.

data = None

if data:
    print("Data exists")
else:
    print("Data is None or empty")


# ===========================================================================
# 🔀 8. None vs False vs 0 vs Empty
# ===========================================================================
# These values are different, even if they behave similarly in conditions.

print(None == False)
print(None == 0)
print(None == "")


# ===========================================================================
# 🧼 9. Best Practices
# ===========================================================================
# ✔ Use None to represent "no value"
# ✔ Use is / is not for comparison
# ✔ Document functions that may return None
# ✔ Check for None before using a value
# ✔ Be explicit and intentional


# ===========================================================================
# 🧠 10. Summary
# ===========================================================================
# In this module, I learned:
# - What None represents
# - That None has its own type: NoneType
# - How functions return None by default
# - How to safely compare with None
# - Common mistakes and best practices


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
# ===========================================================================
