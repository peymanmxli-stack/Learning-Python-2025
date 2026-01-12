"""
⛔ Loop Control Statements — break / continue / pass
Tasks Solutions File (Rank 1 → Rank 5)

This file contains one possible correct and clean solution
for each task in Loop_Control_Tasks.py.
"""


# ===========================================================================
# 🟢 Rank 1 — Beginner
# ===========================================================================

# Task 1:
for number in range(1, 10):
    if number == 5:
        break
    print(number)


# Task 2:
for number in range(1, 6):
    if number == 3:
        continue
    print(number)


# Task 3:
x = 10
if x > 0:
    pass  # Logic will be added later



# ===========================================================================
# 🟡 Rank 2 — Easy
# ===========================================================================

# Task 4:
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)


# Task 5:
counter = 1
while True:
    if counter == 4:
        break
    print(counter)
    counter += 1


# Task 6:
values = [10, None, 5, None, 20]

for value in values:
    if value is None:
        continue
    print(value)



# ===========================================================================
# 🟠 Rank 3 — Intermediate
# ===========================================================================

# Task 7:
numbers = [2, 4, 6, 7, 8]

for n in numbers:
    if n == 7:
        print("Found")
        break


# Task 8:
for number in range(1, 21):
    if number % 3 == 0:
        continue
    if number > 15:
        break
    print(number)


# Task 9:
number = 51
while True:
    if number % 9 == 0:
        print(number)
        break
    number += 1



# ===========================================================================
# 🔴 Rank 4 — Advanced
# ===========================================================================

# Task 10:
while True:
    value = int(input("Enter a number (0 to stop): "))

    if value == 0:
        break
    if value < 0:
        continue

    print(value)


# Task 11:
for i in range(5):
    pass  # TODO: implement retry logic here in the future


# Task 12:
users = ["peyman", "", "nova", "admin", "test"]

for user in users:
    if user == "":
        continue
    if user == "admin":
        print("Admin found")
        break
    print(user)



# ===========================================================================
# 🟣 Rank 5 — Professional
# ===========================================================================

# Task 13:
valid_count = 0

while valid_count < 3:
    number = int(input("Enter a positive number: "))

    if number <= 0:
        continue

    print("Valid:", number)
    valid_count += 1


# Task 14:
logs = ["INFO", "DEBUG", "WARNING", "DEBUG", "ERROR", "CRITICAL", "INFO"]

for log in logs:
    if log == "DEBUG":
        continue
    if log == "CRITICAL":
        print("Critical issue detected!")
        break
    print(log)


# Task 15:
passwords = ["abc", "password", "admin", "pass123", "root"]

for password in passwords:
    if len(password) < 6:
        continue
    if any(char.isdigit() for char in password):
        print("Valid password found:", password)
        break
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
