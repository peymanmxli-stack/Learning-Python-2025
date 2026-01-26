"""
====================================================
PYTHON BUILT-IN COLLECTIONS
TASKS — SOLUTIONS
====================================================

This file contains complete and professional
solutions for all Built-in Collections tasks:

- list
- tuple
- str
- range
- set

Difficulty progresses from Rank 1 (Easy)
to Rank 5 (Professional).

====================================================
"""

# ====================================================
# 🟢 RANK 1 — VERY EASY (SOLUTIONS)
# ====================================================

# Task 1 (List)
numbers = [1, 2, 3]
print(numbers)

# Task 2 (Tuple)
person = ("Peyman", 43)
print(person)

# Task 3 (String)
message = "Welcome to Python Programming!"
print(message)

# Task 4 (Range)
numbers_range = list(range(1, 6))
print(numbers_range)

# Task 5 (Set)
unique_values = {10, 20, 30}
print(unique_values)


# ====================================================
# 🟡 RANK 2 — EASY (SOLUTIONS)
# ====================================================

# Task 6 (List)
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

# Task 7 (Tuple)
cities = ("Mexico City", "Tijuana", "Ensenada")
print(cities[1])

# Task 8 (String)
full_name = "Peyman Miyandashti"
print(len(full_name))

# Task 9 (Range)
for number in range(10):
    print(number)

# Task 10 (Set)
duplicate_set = {1, 2, 2, 3, 3}
print(duplicate_set)


# ====================================================
# 🟠 RANK 3 — INTERMEDIATE (SOLUTIONS)
# ====================================================

# Task 11 (List)
scores = [85, 90, 78, 88]
scores[2] = 82
print(scores)

# Task 12 (Tuple)
rgb = (255, 128, 64)
print(rgb[0], rgb[1], rgb[2])

# Task 13 (String)
email = "user@example.com"
domain = email.split("@")[1]
print(domain)

# Task 14 (Range)
even_numbers = list(range(2, 21, 2))
print(even_numbers)

# Task 15 (Set)
skills_a = {"Python", "Networking", "Security"}
skills_b = {"Python", "Cloud", "Security"}
common_skills = skills_a & skills_b
print(common_skills)


# ====================================================
# 🔵 RANK 4 — ADVANCED (SOLUTIONS)
# ====================================================

# Task 16 (List)
tasks = ["Study", "Code", "Exercise"]
tasks.remove("Exercise")
print(tasks)

# Task 17 (Tuple)
user_info = ("admin", "administrator", "active")
print(f"User '{user_info[0]}' has role '{user_info[1]}' and status '{user_info[2]}'.")

# Task 18 (String)
sentence = "Python programming is powerful"
letter_count = sentence.count("o")
print(letter_count)

# Task 19 (Range)
total = 0
for num in range(1, 101):
    total += num
print(total)

# Task 20 (Set)
authorized_users = {"admin", "manager", "editor"}
user = "admin"
print(user in authorized_users)


# ====================================================
# 🔴 RANK 5 — PROFESSIONAL (SOLUTIONS)
# ====================================================

# Task 21 (List)
prices = [19.99, 5.50, 3.75]
total_price = sum(prices)
print(total_price)

# Task 22 (Tuple)
config = ("localhost", 8080, "HTTP")
print(f"Server running on {config[0]}:{config[1]} using {config[2]} protocol")

# Task 23 (String)
password = "SecurePass123"
if len(password) >= 8:
    print("Password is strong enough")
else:
    print("Password is too short")

# Task 24 (Range)
for user_id in range(1000, 1011):
    print(user_id)

# Task 25 (Set)
course_a = {"Alice", "Bob", "Charlie"}
course_b = {"Bob", "Diana", "Charlie"}
both_courses = course_a & course_b
print(both_courses)


# ====================================================
# END OF SOLUTIONS — BUILT-IN COLLECTIONS
# ====================================================

"""
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
"""
