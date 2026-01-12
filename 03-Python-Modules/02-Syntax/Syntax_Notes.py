"""
📘 Module — Python Syntax
Professional Notes

Syntax is the set of rules that defines how Python code must be written.
Correct syntax allows Python to understand and execute instructions.

This module introduces Python’s core syntax rules, structure, and formatting
conventions. Mastering syntax is essential before writing complex logic,
functions, or programs.
"""


# ===========================================================================
# 🧵 1. What Is Syntax?
# ===========================================================================
# Syntax defines:
# - How statements are written
# - How blocks of code are structured
# - How Python knows where code starts and ends
#
# Incorrect syntax causes SyntaxError and stops execution.


# ===========================================================================
# 🧱 2. Indentation (VERY IMPORTANT)
# ===========================================================================
# Python uses indentation instead of braces {} to define code blocks.

if True:
    print("This line is correctly indented")

# ❌ Incorrect indentation causes an error:
# if True:
# print("Error")


# ===========================================================================
# 🧾 3. Statements and Lines
# ===========================================================================
# A statement is a single instruction.

x = 10
print(x)

# Multiple statements should be written on separate lines.
# Avoid writing multiple statements on one line.


# ===========================================================================
# 🔚 4. Line Breaks and Continuation
# ===========================================================================
# Long lines can be continued using parentheses.

total = (
    10 +
    20 +
    30
)

print(total)


# ===========================================================================
# 📝 5. Comments
# ===========================================================================
# Comments explain code and are ignored by Python.

# This is a single-line comment

"""
This is a multi-line string.
Often used as documentation (docstrings).
"""


# ===========================================================================
# 🧩 6. Variables and Assignment Syntax
# ===========================================================================
# Variables are created by assignment.

name = "Peyman"
age = 43
height = 1.75

print(name, age, height)


# ===========================================================================
# 🔤 7. Naming Rules (Identifiers)
# ===========================================================================
# ✔ Can contain letters, numbers, and underscores
# ✔ Cannot start with a number
# ✔ Cannot use Python keywords
# ✔ Case-sensitive

user_name = "admin"
_user_id = 123

# ❌ Invalid:
# 2name = "error"
# class = "error"


# ===========================================================================
# 🧠 8. Keywords
# ===========================================================================
# Keywords are reserved words in Python.

# Examples:
# if, else, elif, for, while, def, return, True, False, None, import

# They cannot be used as variable names.


# ===========================================================================
# 🧮 9. Expressions
# ===========================================================================
# An expression produces a value.

result = 10 + 5
comparison = 10 > 3
text = "Py" + "thon"

print(result, comparison, text)


# ===========================================================================
# 🧰 10. Blocks of Code
# ===========================================================================
# Blocks start after a colon (:)
# Indentation defines the block.

for i in range(3):
    print("Iteration:", i)

print("Loop finished")


# ===========================================================================
# ⛔ 11. Common Syntax Errors
# ===========================================================================
# ❌ Missing colon
# if x > 5
#     print("Error")

# ❌ Inconsistent indentation
# ❌ Unclosed quotes
# ❌ Misspelled keywords


# ===========================================================================
# ✅ 12. Best Practices
# ===========================================================================
# ✔ Use consistent indentation (4 spaces)
# ✔ Write readable code
# ✔ Use comments when logic is not obvious
# ✔ Follow PEP 8 style guidelines
# ✔ Let your editor highlight syntax errors


# ===========================================================================
# 🧠 13. Summary
# ===========================================================================
# In this module, I learned:
# - What Python syntax is
# - Why indentation matters
# - How statements and blocks work
# - How to write valid variable names
# - Common syntax mistakes to avoid
# - Best practices for clean, readable code
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
