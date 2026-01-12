"""
🔀 Module — Control Flow in Python
📘 Professional Notes

Control flow defines how a Python program executes:
- which code runs
- when it runs
- how often it runs
- how errors and special conditions are handled

This file provides a structured overview of Python control flow,
with explanations, examples, and best practices.
"""


# ===========================================================================
# ✅ 1. Control Flow Basics — if / elif / else
# ===========================================================================

# Conditional statements allow decision-making in code.

age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Conditions are based on boolean expressions.
# Use comparison operators: == != < > <= >=
# Combine conditions with: and, or, not


# ===========================================================================
# 🔁 2. Loops — for / while
# ===========================================================================

# for-loop: iterate over a sequence
for letter in "Python":
    print(letter)

# while-loop: repeat while condition is True
count = 0
while count < 3:
    print("Count:", count)
    count += 1


# ===========================================================================
# 🛑 3. Loop Control Statements
# ===========================================================================

# break — exit the loop completely
for i in range(5):
    if i == 3:
        break
    print("break example:", i)

# continue — skip current iteration
for i in range(5):
    if i == 2:
        continue
    print("continue example:", i)

# pass — placeholder (does nothing)
for i in range(3):
    if i == 1:
        pass  # useful when structure is needed but logic comes later
    print("pass example:", i)


# ===========================================================================
# ⚠️ 4. Exception Handling — try / except / else / finally
# ===========================================================================

# Exceptions prevent programs from crashing unexpectedly.

try:
    number = int("10")
    result = 10 / number
except ValueError:
    print("Conversion failed")
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Result:", result)
finally:
    print("Execution completed")

# finally always runs, whether an exception occurs or not.


# ===========================================================================
# 📦 5. Context Managers — with
# ===========================================================================

# Context managers handle setup and cleanup automatically.

# Example with file handling:
try:
    with open("example.txt", "w") as file:
        file.write("Hello, Control Flow!")
except IOError:
    print("File operation failed")

# 'with' ensures the file is closed properly.


# ===========================================================================
# 🔄 6. Function Flow — return
# ===========================================================================

# return exits a function and optionally sends back a value.

def add(a, b):
    return a + b

sum_result = add(3, 5)
print("Sum:", sum_result)


# ===========================================================================
# 🌊 7. Function Flow — yield (Generators)
# ===========================================================================

# yield creates a generator that produces values lazily.

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

for num in count_up_to(3):
    print("Yielded:", num)


# ===========================================================================
# 🚨 8. Function Flow — raise
# ===========================================================================

# raise allows manual error signaling.

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    withdraw(100, 150)
except ValueError as error:
    print("Error:", error)


# ===========================================================================
# 🧩 9. Pattern Matching — match / case (Python 3.10+)
# ===========================================================================

status_code = 404

match status_code:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")

# Pattern matching is cleaner than long if/elif chains.


# ===========================================================================
# ⚡ 10. Comprehensions
# ===========================================================================

# List comprehension
squares = [x ** 2 for x in range(5)]
print(squares)

# Dictionary comprehension
square_map = {x: x ** 2 for x in range(5)}
print(square_map)

# Set comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hi"]}
print(unique_lengths)


# ===========================================================================
# ❓ 11. Ternary Expressions
# ===========================================================================

# Short conditional expressions (inline if/else)

temperature = 30
message = "Hot" if temperature > 25 else "Cool"
print(message)


# ===========================================================================
# ✅ 12. Best Practices
# ===========================================================================

# ✔ Keep conditions readable
# ✔ Avoid deeply nested if-statements
# ✔ Use early returns in functions
# ✔ Catch only expected exceptions
# ✔ Prefer with for resource handling
# ✔ Use comprehensions wisely (readability first)
# ✔ Use match/case for complex decision trees


# ===========================================================================
# 🧠 13. Summary
# ===========================================================================

# In this module, I learned:
# - How to control execution with conditions and loops
# - How to manage loops with break, continue, and pass
# - How to handle errors safely using exceptions
# - How context managers simplify resource handling
# - How functions control flow with return, yield, and raise
# - How pattern matching improves readability
# - How comprehensions and ternary expressions simplify logic


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
# ===========================================================================
