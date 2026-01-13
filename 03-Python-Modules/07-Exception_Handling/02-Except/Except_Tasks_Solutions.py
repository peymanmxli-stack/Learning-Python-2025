"""
🚨 Exception Handling — except Statement
Tasks Solutions File (Rank 1 → Rank 5)

This file contains correct, clean, and professional solutions
for mastering the `except` keyword in Python.
"""


# ===========================================================================
# 🟢 Rank 1 — Beginner
# ===========================================================================

# Task 1
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")


# Task 2
try:
    number = int("abc")
except ValueError:
    print("Error: Cannot convert string to integer.")


# Task 3
numbers = [1, 2, 3]

try:
    print(numbers[5])
except IndexError:
    print("Error: List index out of range.")



# ===========================================================================
# 🟡 Rank 2 — Easy
# ===========================================================================

# Task 4
try:
    user_input = int(input("Enter an integer: "))
    print("You entered:", user_input)
except ValueError:
    print("Error: Invalid integer input.")


# Task 5
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")


# Task 6
values = ["10", "x", None, "5"]

for value in values:
    try:
        print(int(value))
    except ValueError:
        print("ValueError: Cannot convert value.")
    except TypeError:
        print("TypeError: Invalid type encountered.")



# ===========================================================================
# 🟠 Rank 3 — Intermediate
# ===========================================================================

# Task 7
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero."

print(divide(10, 0))


# Task 8
try:
    num = int(input("Enter a number: "))
    print("Success! You entered:", num)
except ValueError:
    print("Error: Invalid number.")


# Task 9
data = [5, "a", 10, None, 3]
total = 0

for item in data:
    try:
        total += item
    except TypeError:
        print(f"Skipping invalid item: {item}")

print("Total:", total)



# ===========================================================================
# 🔴 Rank 4 — Advanced
# ===========================================================================

# Task 10
while True:
    try:
        number = int(input("Enter an integer (or Ctrl+C to stop): "))
        print("Valid number:", number)
    except ValueError:
        print("Invalid input. Try again.")


# Task 11
try:
    value = int(input("Enter a number: "))
except (ValueError, TypeError):
    print("Error: Invalid input.")


# Task 12
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Handled division error.")

print("Program continues running normally.")



# ===========================================================================
# 🟣 Rank 5 — Professional
# ===========================================================================

# Task 13
try:
    result = 10 / 0
except ZeroDivisionError as error:
    print("Error occurred:", error)


# Task 14
files = ["a.txt", "b.txt", "c.txt"]

for filename in files:
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File not found: {filename}")


# Task 15
try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        raise ValueError("Invalid operator.")

except ZeroDivisionError:
    print("Error: Division by zero.")
except ValueError as err:
    print("Error:", err)


# ===========================================================================
# ✅ End of Solutions
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
🏁 End of Examples
