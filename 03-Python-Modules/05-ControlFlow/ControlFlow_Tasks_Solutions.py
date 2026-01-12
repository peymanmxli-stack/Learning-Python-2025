"""
🔀 Module — Control Flow in Python
✅ Tasks Solutions (Rank 1 → Rank 5)

This file contains one possible set of clean, correct, and professional
solutions for each task in ControlFlow_Tasks.py.
"""


# ===========================================================================
# 🟢 Rank 1 — Beginner
# ===========================================================================

# Task 1 Solution
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Task 2 Solution
for i in range(1, 6):
    print(i)


# Task 3 Solution
count = 5
while count >= 1:
    print(count)
    count -= 1


# ===========================================================================
# 🟡 Rank 2 — Easy
# ===========================================================================

# Task 4 Solution
for number in range(1, 11):
    if number == 5:
        break
    print(number)


# Task 5 Solution
for number in range(1, 6):
    if number == 3:
        continue
    print(number)


# Task 6 Solution
for _ in range(3):
    pass
    print("Loop executed")


# ===========================================================================
# 🟠 Rank 3 — Intermediate
# ===========================================================================

# Task 7 Solution
values = ["10", "x", "5"]

converted_numbers = []
for v in values:
    try:
        converted_numbers.append(int(v))
    except ValueError:
        print(f"Invalid value skipped: {v}")

print(converted_numbers)


# Task 8 Solution
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))


# Task 9 Solution
try:
    with open("controlflow_tasks.txt", "w") as file:
        file.write("Control Flow Tasks File")
    print("File written successfully")
except IOError:
    print("File error occurred")


# ===========================================================================
# 🔴 Rank 4 — Advanced
# ===========================================================================

# Task 10 Solution
def even_numbers(n):
    return [i for i in range(1, n + 1) if i % 2 == 0]

print(even_numbers(10))


# Task 11 Solution
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(5):
    print(value)


# Task 12 Solution
def check_positive(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    return number

try:
    print(check_positive(10))
    print(check_positive(-5))
except ValueError as error:
    print("Error:", error)


# ===========================================================================
# 🔵 Rank 5 — Professional
# ===========================================================================

# Task 13 Solution
command = "restart"

match command:
    case "start":
        print("System starting")
    case "stop":
        print("System stopping")
    case "restart":
        print("System restarting")
    case _:
        print("Unknown command")


# Task 14 Solution
squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares)


# Task 15 Solution
temperature = 30
status = "Hot" if temperature > 25 else "Cool"
print(status)


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
