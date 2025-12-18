"""
📘 Module — Basic Data Types: String (str)
Professional Notes

Strings represent text in Python. They are used everywhere: printing messages,
handling user input, storing names, parsing files, processing data, building
APIs, formatting output, and more.

Python strings are powerful, flexible, and come with many built-in methods.
This file provides a structured overview with examples and best practices.
"""


# ===========================================================================
# 🧵 1. What Is a String?
# ===========================================================================
# A string (str) is a sequence of characters enclosed in quotes.
# You can use:
#   - single quotes    'Hello'
#   - double quotes    "Hello"
#   - triple quotes    """Multi-line text"""

name1 = 'Peyman'
name2 = "Arlette"
message = """This is
a multi-line string."""

print(name1, name2)
print(message)


# ===========================================================================
# 🔢 2. Strings Are Sequences (Indexing & Slicing)
# ===========================================================================
# Strings behave like lists of characters.

# Indexing:
text = "Python"
print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n (last character)

# Slicing:
print(text[0:3])   # Pyt
print(text[:4])    # Pyth
print(text[2:])    # thon
print(text[::-1])  # reverse string


# ===========================================================================
# 🔒 3. String Immutability
# ===========================================================================
# Strings cannot be changed after creation.
# ❌ text[0] = "X"  → ERROR
#
# ✔ You must create a new string instead:
new_text = "J" + text[1:]
print(new_text)


# ===========================================================================
# ➕ 4. Basic String Operations
# ===========================================================================

# Concatenation:
greeting = "Hello" + " " + "World"
print(greeting)

# Repetition:
print("ha" * 3)

# Length:
print("Length of 'Python':", len(text))

# Membership:
print("P" in text)
print("z" in text)


# ===========================================================================
# 🧰 5. Common String Methods
# ===========================================================================
s = "  Python Programming  "

print(s.lower())        # convert to lowercase
print(s.upper())        # convert to uppercase
print(s.strip())        # remove whitespace
print(s.replace("Python", "Java"))
print(s.startswith("  Py"))
print(s.endswith("ing  "))

# Splitting and joining:
words = s.split()       # split into list
print(words)

joined = "-".join(words)
print(joined)


# ===========================================================================
# ⛔ 6. Escape Characters
# ===========================================================================
# Escape characters allow special symbols inside strings.

print("Line 1\nLine 2")      # newline
print("She said \"Hello\"")  # quotes inside quotes
print("Tab\tSpacing")        # tab


# ===========================================================================
# ✨ 7. f-Strings (Recommended for Formatting)
# ===========================================================================
# f-strings are the modern, clean way to format text.

user = "Peyman"
age = 43
print(f"My name is {user} and I am {age} years old.")

value = 3.14159
print(f"Value rounded to 2 decimals: {value:.2f}")


# ===========================================================================
# 🔁 8. Looping Through Strings
# ===========================================================================

for char in "Nova":
    print("Letter:", char)


# ===========================================================================
# 🔍 9. Searching & Counting
# ===========================================================================

text2 = "banana"
print(text2.count("a"))      # count occurrences
print(text2.find("na"))      # index of first match
print(text2.rfind("na"))     # index from right
print("na" in text2)         # membership test


# ===========================================================================
# ⚡ 10. Building Strings Efficiently
# ===========================================================================
# Joining lists is faster than repeated concatenation.

parts = []
for i in range(5):
    parts.append(f"Item-{i}")

result = ", ".join(parts)
print(result)


# ===========================================================================
# ✅ 11. Best Practices
# ===========================================================================
# ✔ Use f-strings for formatting — clean and fast
# ✔ Use .strip(), .lower(), .upper() when cleaning user input
# ✔ Use .split() and .join() for text processing
# ✔ Remember strings are immutable — avoid repeated +
# ✔ Use in for simple searches instead of find()
# ✔ Keep strings readable with triple quotes for long text


# ===========================================================================
# 🧠 12. Summary
# ===========================================================================
# In this module, I learned:
# - What strings are and how they behave as sequences
# - How to index and slice text
# - Why strings are immutable
# - Common methods for cleaning and transforming text
# - Formatting text with f-strings
# - Searching, counting, and looping through strings
# - Best practices for writing clean string-based code
# ===========================================================================
#👤 Author
# ===========================================================================
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2025
🆔 ID: 250161
# 🏁 End of Notes
