"""
🧠 Module — Type Objects
📘 Professional Notes

In Python, everything is an object.
Variables do not store values directly — they reference objects.
Each object has:
- a value
- a type
- an identity

Understanding type objects helps explain Python’s dynamic behavior and
prevents many common bugs.
"""


# ===========================================================================
# 🔍 1. Objects and Variables
# ===========================================================================
# Variables are names bound to objects in memory.

x = 10
y = "Python"

# x references an integer object
# y references a string object

print(x)
print(y)


# ===========================================================================
# 🧬 2. Types Are Objects Too
# ===========================================================================
# In Python, types themselves are objects.

print(type(10))        # <class 'int'>
print(type("Hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>

# Even the type "type" is an object:
print(type(int))
print(type(type))


# ===========================================================================
# 🧪 3. Using type()
# ===========================================================================
# type() returns the exact type of an object.

value = 3.14
print(type(value))

# Direct type comparison (not recommended in most cases):
print(type(value) == float)


# ===========================================================================
# ✅ 4. Using isinstance() (Recommended)
# ===========================================================================
# isinstance() checks if an object belongs to a type or its subclasses.

number = 5

print(isinstance(number, int))
print(isinstance(number, bool))  # False

# isinstance supports tuples of types:
print(isinstance(number, (int, float)))


# ===========================================================================
# 🆔 5. Object Identity (id)
# ===========================================================================
# id() returns the identity of an object (memory address reference).

a = 100
b = 100

print(id(a))
print(id(b))

# Small integers may share the same identity (optimization).


# ===========================================================================
# 🔁 6. Object References and Reassignment
# ===========================================================================
# Reassigning a variable does NOT change the original object.

x = 10
print(id(x))

x = x + 1
print(id(x))  # New object


# ===========================================================================
# 🧠 7. Value vs Type vs Identity
# ===========================================================================
# value   → what the object represents
# type    → what kind of object it is
# identity → where it exists in memory

value1 = "Python"
value2 = "Python"

print(value1 == value2)     # True (same value)
print(value1 is value2)     # May be True or False (identity)


# ===========================================================================
# ⚠️ 8. Common Beginner Mistakes
# ===========================================================================
# ❌ Using type() instead of isinstance()
# ❌ Confusing 'is' with '=='
# ❌ Assuming variables store values instead of references
# ❌ Ignoring dynamic typing behavior


# ===========================================================================
# 🔒 9. Dynamic Typing in Python
# ===========================================================================
# A variable can reference objects of different types over time.

data = 10
print(type(data))

data = "Ten"
print(type(data))

data = [1, 2, 3]
print(type(data))


# ===========================================================================
# 🧼 10. Best Practices
# ===========================================================================
# ✔ Use isinstance() for type checking
# ✔ Avoid 'is' for value comparison
# ✔ Write flexible, dynamic code
# ✔ Validate inputs when necessary
# ✔ Trust Python’s object model


# ===========================================================================
# 🧠 11. Summary
# ===========================================================================
# In this module, I learned:
# - Variables reference objects, not values
# - Types themselves are objects
# - How to use type(), isinstance(), and id()
# - The difference between value, type, and identity
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
