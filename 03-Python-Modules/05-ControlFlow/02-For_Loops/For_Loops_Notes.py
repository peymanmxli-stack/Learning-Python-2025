"""
🔁 Control Flow — for Loops
Professional Notes

A for loop allows us to iterate over items in a sequence (iterable)
and execute a block of code for each item.
"""


# ===========================================================================
# 🔹 1. Basic for Loop
# ===========================================================================

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)


# ===========================================================================
# 🔹 2. Looping Over Strings
# ===========================================================================

word = "Python"

for letter in word:
    print(letter)


# ===========================================================================
# 🔹 3. Using range()
# ===========================================================================

# range(stop)
for i in range(5):
    print(i)

# range(start, stop)
for i in range(2, 6):
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)


# ===========================================================================
# 🔹 4. for Loop with Conditional Logic
# ===========================================================================

for number in range(1, 11):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# ===========================================================================
# 🔹 5. Looping Through Lists of Mixed Types
# ===========================================================================

items = ["Python", 3.11, True, None]

for item in items:
    print(item, type(item))


# ===========================================================================
# 🔹 6. enumerate() — Index + Value
# ===========================================================================

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)


# ===========================================================================
# 🔹 7. Looping Through Dictionaries
# ===========================================================================

student = {
    "name": "Peyman",
    "age": 43,
    "career": "IT Engineering"
}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key-value pairs
for key, value in student.items():
    print(key, "=>", value)


# ===========================================================================
# 🔹 8. Nested for Loops
# ===========================================================================

for row in range(1, 4):
    for col in range(1, 4):
        print(f"Row {row}, Column {col}")


# ===========================================================================
# 🔹 9. for Loop with else
# ===========================================================================

for number in range(5):
    print(number)
else:
    print("Loop completed normally")


# ===========================================================================
# 🔹 10. Common Mistakes
# ===========================================================================

# ❌ Modifying a list while iterating over it
# ❌ Using range(len(list)) when enumerate() is clearer
# ❌ Deep nesting instead of breaking logic into functions


# ===========================================================================
# ✅ Best Practices Summary
# ===========================================================================

# ✔ Use for loops for iteration
# ✔ Use enumerate() for index access
# ✔ Use clear variable names
# ✔ Keep loops short and readable
# ✔ Combine with if statements when needed


# ===========================================================================
# 🧠 Summary
# ===========================================================================

# In this module, I learned:
# - How for loops work in Python
# - How to iterate over sequences and ranges
# - How to access indexes cleanly
# - How to loop through dictionaries
# - How and when to use for-else
# - Best practices for professional Python code


# ===========================================================================
# 👤 Author
# ===========================================================================
👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
