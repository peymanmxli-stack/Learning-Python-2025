"""
🔀 Module — Control Flow in Python
📂 Examples File

This file contains focused, runnable examples demonstrating how
Python control flow works in real programs.

How to use this file:
- Run it with:  python ControlFlow_Examples.py
- Read comments before each example
- Modify values to observe different execution paths
"""


# ===========================================================================
# Example 1 — if / elif / else
# ===========================================================================
score = 78

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# ===========================================================================
# Example 2 — for Loop
# ===========================================================================
for i in range(3):
    print("for loop iteration:", i)


# ===========================================================================
# Example 3 — while Loop
# ===========================================================================
count = 0
while count < 3:
    print("while loop count:", count)
    count += 1


# ===========================================================================
# Example 4 — break
# ===========================================================================
for number in range(10):
    if number == 5:
        print("Breaking at:", number)
        break
    print("Number:", number)


# ===========================================================================
# Example 5 — continue
# ===========================================================================
for number in range(5):
    if number == 2:
        continue
    print("Processed:", number)


# ===========================================================================
# Example 6 — pass
# ===========================================================================
for i in range(3):
    if i == 1:
        pass
    print("Loop value:", i)


# ===========================================================================
# Example 7 — try / except
# ===========================================================================
values = ["10", "x", "5"]

for v in values:
    try:
        number = int(v)
        print("Converted:", number)
    except ValueError:
        print("Conversion failed for:", v)


# ===========================================================================
# Example 8 — try / except / finally
# ===========================================================================
try:
    x = 10 / 2
    print("Result:", x)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Finished calculation")


# ===========================================================================
# Example 9 — with (Context Manager)
# ===========================================================================
try:
    with open("controlflow_example.txt", "w") as file:
        file.write("Control Flow Example")
    print("File written successfully")
except IOError:
    print("File operation error")


# ===========================================================================
# Example 10 — return
# ===========================================================================
def multiply(a, b):
    return a * b

print("Multiply result:", multiply(4, 5))


# ===========================================================================
# Example 11 — yield (Generator)
# ===========================================================================
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(3):
    print("Countdown:", value)


# ===========================================================================
# Example 12 — raise
# ===========================================================================
def login_attempts(attempts):
    if attempts > 3:
        raise RuntimeError("Too many login attempts")
    return "Access granted"

try:
    print(login_attempts(4))
except RuntimeError as error:
    print("Error:", error)


# ===========================================================================
# Example 13 — match / case
# ===========================================================================
command = "start"

match command:
    case "start":
        print("System starting")
    case "stop":
        print("System stopping")
    case "restart":
        print("System restarting")
    case _:
        print("Unknown command")


# ===========================================================================
# Example 14 — Comprehensions
# ===========================================================================
numbers = [1, 2, 3, 4, 5]

squares = [n ** 2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]

print("Squares:", squares)
print("Evens:", even_numbers)


# ===========================================================================
# Example 15 — Ternary Expression
# ===========================================================================
temperature = 18
status = "Cold" if temperature < 20 else "Warm"
print("Weather:", status)


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
