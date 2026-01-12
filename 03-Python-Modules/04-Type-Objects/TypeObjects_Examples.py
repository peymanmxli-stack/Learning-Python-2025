"""
🧠 Module — Type Objects
📂 Examples File

This file contains practical examples that demonstrate how Python
handles objects, types, identity, and dynamic typing.

Run this file and observe the output carefully.
"""


# ===========================================================================
# 🔍 1. Inspecting Types with type()
# ===========================================================================

a = 10
b = 3.14
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# ===========================================================================
# 🧬 2. Types Are Objects
# ===========================================================================
# Types themselves have types.

print(type(int))
print(type(str))
print(type(bool))
print(type(type))


# ===========================================================================
# ✅ 3. Safe Type Checking with isinstance()
# ===========================================================================

value = 42

print(isinstance(value, int))
print(isinstance(value, float))
print(isinstance(value, bool))
print(isinstance(value, (int, float)))


# ===========================================================================
# 🆔 4. Object Identity with id()
# ===========================================================================
# id() returns a unique identifier for an object.

x = 100
y = 100

print(id(x))
print(id(y))


# ===========================================================================
# 🔁 5. Identity Changes on Reassignment
# ===========================================================================

num = 10
print("Before:", id(num))

num = num + 1
print("After:", id(num))


# ===========================================================================
# 🧠 6. Value Equality vs Identity
# ===========================================================================
# == checks value
# is checks identity

s1 = "hello"
s2 = "hello"

print(s1 == s2)
print(s1 is s2)


# ===========================================================================
# 🔀 7. Dynamic Typing Example
# ===========================================================================

data = 100
print(data, type(data))

data = "one hundred"
print(data, type(data))

data = [1, 2, 3]
print(data, type(data))


# ===========================================================================
# ⚠️ 8. Common Mistake: Using type() Incorrectly
# ===========================================================================
# This works but is NOT recommended:

value = 5
print(type(value) == int)

# Preferred approach:
print(isinstance(value, int))


# ===========================================================================
# 🧪 9. isinstance() with Multiple Types
# ===========================================================================

item = 3.5

if isinstance(item, (int, float)):
    print("Item is numeric")


# ===========================================================================
# 🔍 10. Objects Passed by Reference
# ===========================================================================

list_a = [1, 2, 3]
list_b = list_a

print(id(list_a))
print(id(list_b))

list_b.append(4)

print(list_a)
print(list_b)


# ===========================================================================
# 🧼 11. Clean, Defensive Type Checking
# ===========================================================================

def add_numbers(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    return "Invalid input types"

print(add_numbers(5, 3))
print(add_numbers("5", 3))


# ===========================================================================
# 🧠 12. Key Takeaways
# ===========================================================================
# ✔ Everything in Python is an object
# ✔ Variables reference objects
# ✔ type() inspects exact types
# ✔ isinstance() is safer and more flexible
# ✔ id() reveals object identity
# ✔ == compares values, is compares identity


# ===========================================================================
# 🏁 End of Examples
# ===========================================================================
