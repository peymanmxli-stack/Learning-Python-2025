"""
⭕ Module — NoneType (None)
📂 Examples File

This file contains practical, runnable examples that demonstrate how
None is used in real Python programs.

How to use this file:
- Run it with:  python NoneType_Examples.py
- Read the comments before each example
- Modify values to observe different behaviors
"""


# ===========================================================================
# Example 1 — Assigning None
# ===========================================================================
value = None
print(value)
print(type(value))


# ===========================================================================
# Example 2 — None as a Default Placeholder
# ===========================================================================
user_email = None

if user_email is None:
    print("Email not provided yet")


# ===========================================================================
# Example 3 — Functions Returning None
# ===========================================================================
def print_message(msg):
    print(msg)

result = print_message("Hello from a function")
print("Returned value:", result)


# ===========================================================================
# Example 4 — None vs Other “Empty” Values
# ===========================================================================
values = [None, False, 0, "", [], {}]

for v in values:
    print(f"Value: {v!r:<6} | Type: {type(v).__name__}")


# ===========================================================================
# Example 5 — Checking None Correctly
# ===========================================================================
data = None

if data is None:
    print("Data is None (correct check)")


# ===========================================================================
# Example 6 — None in Conditional Logic
# ===========================================================================
response = None

if response:
    print("Response exists")
else:
    print("Response is None or empty")


# ===========================================================================
# Example 7 — Updating a None Value
# ===========================================================================
score = None
print("Before:", score)

score = 85
print("After:", score)


# ===========================================================================
# Example 8 — Searching and Returning None
# ===========================================================================
def find_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None

result = find_even([1, 3, 5, 7])
print("Found:", result)


# ===========================================================================
# Example 9 — Safe Use of None with Guards
# ===========================================================================
name = None

if name is not None:
    print(name.upper())
else:
    print("Name not set")


# ===========================================================================
# Example 10 — None as a Sentinel Value
# ===========================================================================
def load_config(path=None):
    if path is None:
        return "Using default configuration"
    return f"Loading config from {path}"

print(load_config())
print(load_config("config.json"))


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
