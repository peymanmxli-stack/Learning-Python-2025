"""
⭕ Module — NoneType (None)
✅ Tasks Solutions (Rank 1 → Rank 5)

This file contains one possible set of correct and clean solutions
for each task in NoneType_Tasks.py.

These solutions prioritize:
- Correct use of `is None`
- Readable, professional Python code
- Safe handling of missing values
"""


# ===========================================================================
# 🟢 Rank 1 — Beginner
# ===========================================================================

# Task 1 Solution
result = None
print(result)
print(type(result))


# Task 2 Solution
value = None

if value is None:
    print("Value is None")


# Task 3 Solution
def do_nothing():
    print("This function does something but returns nothing")

returned_value = do_nothing()
print("Returned value:", returned_value)


# ===========================================================================
# 🟡 Rank 2 — Easy
# ===========================================================================

# Task 4 Solution
number = None

if number is None:
    print("No number available")
else:
    print(number * 2)


# Task 5 Solution
values = [None, False, 0, ""]

for v in values:
    print(f"Value: {v!r:<5} | Type: {type(v).__name__}")


# ===========================================================================
# 🟠 Rank 3 — Intermediate
# ===========================================================================

# Task 6 Solution
def find_name(names):
    if not names:
        return None
    return names[0]

print(find_name([]))
print(find_name(["Peyman", "Arlette"]))


# Task 7 Solution
items = [1, None, 3, None, 5]

for item in items:
    if item is not None:
        print(item)


# Task 8 Solution
def count_keys(data):
    if not data:
        return None
    return len(data)

print(count_keys({}))
print(count_keys({"a": 1, "b": 2}))


# ===========================================================================
# 🔴 Rank 4 — Advanced
# ===========================================================================

# Task 9 Solution
def safe_divide(a, b):
    if b is None or b == 0:
        return None
    return a / b

print(safe_divide(10, None))
print(safe_divide(10, 0))
print(safe_divide(10, 2))


# Task 10 Solution
user_input = None

if user_input is None:
    user_input = "Default Value"

print(user_input)


# ===========================================================================
# 🔵 Rank 5 — Professional
# ===========================================================================

# Task 11 Solution
def get_config(path=None):
    if path is None:
        return "Default configuration loaded"
    return f"Configuration loaded from {path}"

print(get_config())
print(get_config("settings.yaml"))


# Task 12 Solution
def find_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None

result = find_even([1, 3, 5])

if result is not None:
    print("Found even number:", result)
else:
    print("No even number found")


# Task 13 Solution
test_value = None

# ❌ Not recommended
if test_value == None:
    print("Checked with ==")

# ✔ Recommended
if test_value is None:
    print("Checked with is (correct)")


# ===========================================================================
# 👤 Author
# ===========================================================================
👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161

# 🏁 End of Solutions
# ===========================================================================
