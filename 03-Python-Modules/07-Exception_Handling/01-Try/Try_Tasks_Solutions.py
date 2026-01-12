"""
🚨 Exception Handling — try Statement
Tasks Solutions (Rank 1 → Rank 5)

These solutions demonstrate correct placement and usage of try blocks.
Generic except is used intentionally for learning purposes.
"""


# ===========================================================================
# 🟢 Rank 1 — Beginner
# ===========================================================================

# Task 1 Solution
try:
    result = 10 / 2
    print(result)
except:
    print("Error during division")


# Task 2 Solution
try:
    number = int("123")
    print(number)
except:
    print("Conversion failed")


# Task 3 Solution
items = [1, 2, 3]

try:
    print(items[10])
except:
    print("Index error")



# ===========================================================================
# 🟡 Rank 2 — Easy
# ===========================================================================

# Task 4 Solution
try:
    user_input = input("Enter a number: ")
    value = int(user_input)
    print("Valid input:", value)
except:
    print("Invalid input")


# Task 5 Solution
try:
    file = open("data.txt", "r")
    print(file.read())
except:
    print("File could not be opened")


# Task 6 Solution
values = ["10", "x", None, "5"]

for v in values:
    try:
        print(int(v))
    except:
        print("Conversion error")



# ===========================================================================
# 🟠 Rank 3 — Intermediate
# ===========================================================================

# Task 7 Solution
def safe_multiply(a, b):
    try:
        return a * b
    except:
        return "Error in multiplication"


print(safe_multiply(3, 4))


# Task 8 Solution
while True:
    try:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        print("Number:", num)
    except:
        print("Invalid input")


# Task 9 Solution
try:
    x = int("5")
    y = int("0")
    print(x / y)
except:
    print("Operation failed")



# ===========================================================================
# 🔴 Rank 4 — Advanced
# ===========================================================================

# Task 10 Solution
values = ["10", "x", "5"]

for v in values:
    try:
        print(int(v))
    except:
        print("Error, continuing loop")


# Task 11 Solution
try:
    a = 10
    b = 0
    print(a / b)
except:
    print("Calculation error")


# Task 12 Solution
try:
    print("Inside try block")
    result = 5 / 0
except:
    print("Error inside try")

print("Outside try block")



# ===========================================================================
# 🟣 Rank 5 — Professional
# ===========================================================================

# Task 13 Solution
try:
    user_input = input("Enter age: ")
    age = int(user_input)
    print("Age:", age)
except:
    print("Invalid age")


# Task 14 Solution
files = ["a.txt", "b.txt", "c.txt"]

for file_name in files:
    try:
        file = open(file_name, "r")
        print(file.read())
    except:
        print(f"Failed to open {file_name}")


# Task 15 Solution
try:
    value = int(input("Enter a number: "))
    print("Square:", value ** 2)
except:
    print("Unexpected input error")
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
