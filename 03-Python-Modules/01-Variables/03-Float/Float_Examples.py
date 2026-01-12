"""
📂 Module — Basic Data Types: Float (float)
📘 Examples File

This file contains focused, runnable examples that demonstrate how
floating-point numbers work in Python.

How to use this file:
- Run it with:  python Float_Examples.py
- Observe the output carefully.
- Modify values and experiment with calculations.
"""


# ===========================================================================
# 🔹 Example 1: Creating Float Values
# ===========================================================================
price = 19.99
temperature = -3.5
pi = 3.14159

print(price)
print(temperature)
print(pi)
print(type(price))


# ===========================================================================
# 🔹 Example 2: Integers vs Floats
# ===========================================================================
a = 10
b = 10.0

print(a, type(a))
print(b, type(b))
print(a == b)   # values are equal
print(type(a) == type(b))  # types are different


# ===========================================================================
# 🔹 Example 3: Basic Float Arithmetic
# ===========================================================================
x = 5.5
y = 2.0

print(x + y)
print(x - y)
print(x * y)
print(x / y)


# ===========================================================================
# 🔹 Example 4: Division Always Produces Floats
# ===========================================================================
print(10 / 2)
print(9 / 3)
print(5 / 2)
print(type(10 / 2))


# ===========================================================================
# 🔹 Example 5: Rounding Floats
# ===========================================================================
value = 3.1415926535

print(round(value))
print(round(value, 2))
print(round(value, 4))


# ===========================================================================
# 🔹 Example 6: Floating-Point Precision Issues
# ===========================================================================
# Due to how floats are stored in memory, results may not be exact.

result = 0.1 + 0.2
print(result)
print(result == 0.3)


# ===========================================================================
# 🔹 Example 7: Using Floats in Comparisons
# ===========================================================================
a = 0.3
b = 0.1 + 0.2

print(a == b)
print(abs(a - b) < 0.00001)  # safer comparison


# ===========================================================================
# 🔹 Example 8: Converting Between Types
# ===========================================================================
integer_number = 7
string_number = "4.5"

print(float(integer_number))
print(float(string_number))
print(int(4.9))  # truncates, does not round


# ===========================================================================
# 🔹 Example 9: Floats in Real-World Calculations
# ===========================================================================
price = 49.99
tax_rate = 0.16

tax = price * tax_rate
total = price + tax

print("Tax:", tax)
print("Total:", total)


# ===========================================================================
# 🔹 Example 10: Formatting Floats with f-Strings
# ===========================================================================
total_price = 123.456789

print(f"Total: {total_price}")
print(f"Total (2 decimals): {total_price:.2f}")
print(f"Total (currency): ${total_price:.2f}")


# ===========================================================================
# 🔹 Example 11: Floats in Loops
# ===========================================================================
value = 1.0

while value <= 3.0:
    print("Value:", value)
    value += 0.5


# ===========================================================================
# 🔹 Example 12: Using Floats in Functions
# ===========================================================================
def calculate_circle_area(radius):
    pi = 3.14159
    return pi * radius * radius

print(calculate_circle_area(5))
print(calculate_circle_area(2.5))


# ===========================================================================
# 🔹 Example 13: Avoiding Common Float Mistakes
# ===========================================================================
# ❌ Avoid checking floats for exact equality
# ✔ Prefer tolerance-based comparisons

x = 1.1 + 2.2
y = 3.3

print(abs(x - y) < 1e-9)


# ===========================================================================
# 🏁 End of Examples
# ===========================================================================


# 👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
