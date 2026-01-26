"""
PYTHON COLLECTIONS — PROFESSIONAL EXAMPLES

This file demonstrates real-world, practical usage of Python collections.
Each example is designed to reflect how collections are used in
production-level Python code.
"""

# ==========================================================
# 1️⃣ LIST — EXAMPLES
# ==========================================================

# Example 1: Managing a dynamic list of user names
users = ["Peyman", "Arlette", "Ali"]

# Add a new user
users.append("Sara")

# Remove a user
users.remove("Ali")

# Iterate over users
for user in users:
    print(f"User: {user}")


# Example 2: Collecting numeric data and processing it
grades = [85, 90, 78, 92]

# Calculate average grade
average = sum(grades) / len(grades)

print(f"Average grade: {average}")

# Sort grades
grades.sort()
print("Sorted grades:", grades)

# ==========================================================
# 2️⃣ TUPLE — EXAMPLES
# ==========================================================

# Example 1: Storing fixed configuration values
DATABASE_CONFIG = ("localhost", 5432, "admin")

host, port, username = DATABASE_CONFIG

print(f"Host: {host}")
print(f"Port: {port}")
print(f"User: {username}")


# Example 2: Returning multiple values from a function
def get_coordinates():
    return (10.5, 20.3)

x, y = get_coordinates()
print(f"X: {x}, Y: {y}")

# ==========================================================
# 3️⃣ SET — EXAMPLES
# ==========================================================

# Example 1: Removing duplicate entries from user input
emails = [
    "user1@mail.com",
    "user2@mail.com",
    "user1@mail.com"
]

unique_emails = set(emails)

print("Unique emails:", unique_emails)


# Example 2: Comparing permissions between roles
admin_permissions = {"read", "write", "delete"}
user_permissions = {"read"}

# Find shared permissions
common_permissions = admin_permissions.intersection(user_permissions)

print("Common permissions:", common_permissions)

# ==========================================================
# 4️⃣ DICTIONARY — EXAMPLES
# ==========================================================

# Example 1: Storing user profile information
user_profile = {
    "username": "peyman",
    "age": 43,
    "country": "Mexico",
    "active": True
}

# Access and update data
user_profile["age"] = 44

print("User profile:", user_profile)


# Example 2: Configuration settings for an application
app_settings = {
    "theme": "dark",
    "debug": False,
    "version": "1.0.0"
}

# Safe access using get()
debug_mode = app_settings.get("debug", False)
print("Debug mode:", debug_mode)

# ==========================================================
# 5️⃣ NESTED COLLECTIONS — EXAMPLES
# ==========================================================

# Example 1: List of dictionaries (common in APIs)
users = [
    {"id": 1, "name": "Peyman", "role": "admin"},
    {"id": 2, "name": "Arlette", "role": "user"}
]

for user in users:
    print(f"{user['name']} -> {user['role']}")


# Example 2: Dictionary containing lists
classroom = {
    "teacher": "Arlette",
    "students": ["Peyman", "Ali", "Sara"]
}

print("Teacher:", classroom["teacher"])
print("Students:")
for student in classroom["students"]:
    print("-", student)

# ==========================================================
# 6️⃣ MUTABILITY VS IMMUTABILITY — EXAMPLES
# ==========================================================

# Example 1: Mutable list behavior
scores = [10, 20, 30]

def add_score(data):
    data.append(40)

add_score(scores)
print("Modified scores:", scores)


# Example 2: Immutable tuple behavior
settings = (1920, 1080)

def change_settings(config):
    # This creates a new tuple instead of modifying
    return (config[0], 720)

new_settings = change_settings(settings)

print("Original settings:", settings)
print("New settings:", new_settings)

# ==========================================================
# 7️⃣ PERFORMANCE-AWARE COLLECTION CHOICE — EXAMPLES
# ==========================================================

# Example 1: Fast lookup using set
allowed_users = {"peyman", "admin", "root"}

print("Is user allowed?", "peyman" in allowed_users)


# Example 2: Fast lookup using dictionary
user_roles = {
    "peyman": "admin",
    "arlette": "teacher"
}

role = user_roles.get("peyman")
print("User role:", role)

# ==========================================================
# 👤 Author
# ==========================================================

"""
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
"""
