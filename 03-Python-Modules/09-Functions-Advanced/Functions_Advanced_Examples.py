# Example 1: Default and keyword arguments
def register_user(username, role="student"):
    print(f"{username} registered as {role}")

register_user("Peyman")
register_user("Admin", role="administrator")

# Example 2: *args
def multiply(*values):
    result = 1
    for v in values:
        result *= v
    return result

print(multiply(2, 3, 4))

# Example 3: **kwargs
def create_profile(**data):
    for k, v in data.items():
        print(f"{k}: {v}")

create_profile(name="Peyman", age=43, country="Mexico")

# Example 4: Lambda
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Example 5: Closure
def outer(msg):
    def inner():
        print(msg)
    return inner

hello = outer("Hello from closure")
hello()

👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
