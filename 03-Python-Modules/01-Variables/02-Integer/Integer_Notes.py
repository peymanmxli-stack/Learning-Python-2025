"""
🔢 Module — Basic Data Types: Integer (int)
📘 Professional Notes

This file explains how Python integers work at a deep and practical level.
Integers are used in almost every Python program—counters, IDs, math,
conditions, ranges, time calculations, loops, indexing, and more.

Python’s int type is powerful because it supports unlimited precision,
rich arithmetic operators, type conversion, and even bitwise operations.
"""


# ===========================================================================
# 🔹 1. What Is an Integer?
# ===========================================================================
# An integer (int) is a whole number:
#   - ..., -3, -2, -1, 0, 1, 2, 3, ...
#
# Integers have no decimal part.
# Python automatically chooses int when the value has no fractional part.

a = 10
b = -5
c = 0

print("Basic integers:", a, b, c)


# ===========================================================================
# ♾️ 2. Python Integers Have Unlimited Precision
# ===========================================================================
# In many languages, integers have fixed size (32-bit, 64-bit).
# Python automatically expands the integer size as needed.

huge_number = 10**100  # a googol
print("Huge number example:", huge_number)

# There is no overflow in Python!
# But extremely large integers may affect performance.


# ===========================================================================
# 🔢 3. Creating Integers (Literal Forms)
# ===========================================================================

# Decimal form (normal):
x = 42

# Binary form (prefix 0b):
binary_num = 0b1010  # equals 10

# Octal form (prefix 0o):
octal_num = 0o12  # equals 10

# Hexadecimal form (prefix 0x):
hex_num = 0xA  # equals 10

print("Binary, octal, hex:", binary_num, octal_num, hex_num)


# ===========================================================================
# ➕ 4. Arithmetic Operators (Core Integer Operations)
# ===========================================================================
# +   addition
# -   subtraction
# *   multiplication
# /   floating-point division
# //  floor (integer) division
# %   modulus (remainder)
# **  exponentiation

a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Float division:", a / b)     # returns float
print("Floor division:", a // b)    # returns integer
print("Modulus:", a % b)            # remainder
print("Power:", a ** b)


# ===========================================================================
# ➗ 5. Integer Division: / vs //
# ===========================================================================
# / always returns float
# // returns an integer (floored value)

print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)


# ===========================================================================
# 🔁 6. Converting Values to Integers
# ===========================================================================

print(int("123"))       # convert string → integer
print(int(3.9))         # float → int (truncates toward zero)
print(int(True))        # True → 1
print(int(False))       # False → 0


# ===========================================================================
# 🔂 7. Integers in Loops and Counters
# ===========================================================================

for i in range(5):
    print("Loop index:", i)


# ===========================================================================
# ⚖️ 8. Comparisons and Boolean Results
# ===========================================================================
# Integer comparisons return Boolean values.

print(5 > 2)
print(7 == 7)
print(3 != 3)


# ===========================================================================
# 🧠 9. Bitwise Operations (Binary-Level Integer Logic)
# ===========================================================================
# These are powerful when working with low-level data, permissions,
# masks, compression, and system programming.
#
# &   bitwise AND
# |   bitwise OR
# ^   bitwise XOR
# <<  shift left
# >>  shift right

x = 0b1010  # 10
y = 0b1100  # 12

print("AND:", bin(x & y))
print("OR:", bin(x | y))
print("XOR:", bin(x ^ y))
print("Left shift:", bin(x << 1))   # multiply by 2
print("Right shift:", bin(x >> 1))  # divide by 2


# ===========================================================================
# ⚠️ 10. Common Mistakes with Integers
# ===========================================================================

# ❌ Mixing string numbers and integers incorrectly:
#   "5" + 5 → ERROR
#
# ✔ Correct:
print(int("5") + 5)

# ❌ Using / when you expect an integer
# ✔ Use // for integer division.


# ===========================================================================
# ✅ 11. Best Practices
# ===========================================================================
# ✔ Prefer integers for counters and loop indexes
# ✔ Use // when integer division is required
# ✔ Convert user input with int() explicitly
# ✔ Be careful with very large integers (performance)
# ✔ Use bitwise operators only when needed, keep code readable
# ✔ Use underscores in large numbers for clarity:
large = 1_000_000
print("Readable large integer:", large)


# ===========================================================================
# 🧠 12. Summary
# ===========================================================================
# In this module, I learned:
# - What integers are and how Python stores them
# - How to create integers in decimal, binary, octal, and hex
# - All arithmetic operators, including // and %
# - How to convert types into integers
# - How integers are used in loops and conditions
# - Binary-level (bitwise) operations
# - Important best practices and common mistakes


# ===========================================================================
# 👤 Author
# ===========================================================================
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2025
🆔 ID: 250161

# 🏁 End of Notes
