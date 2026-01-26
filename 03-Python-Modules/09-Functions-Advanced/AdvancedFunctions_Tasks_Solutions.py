"""
ADVANCED FUNCTIONS — TASK SOLUTIONS
"""
1️⃣ Default Arguments — Solutions
def greet(name="User"):
    print(f"Hello {name}")

def power(base, exponent=2):
    return base ** exponent

def calculate_salary(salary, bonus=0):
    return salary + bonus

def send_email(to, subject="No Subject", urgent=False):
    return to, subject, urgent

def create_user(username, role="user", active=True):
    return {"username": username, "role": role, "active": active}
2️⃣ Keyword Arguments — Solutions
def profile(name, age, country):
    return name, age, country

profile(name="Peyman", age=43, country="Mexico")

def order(item, quantity, price):
    return item, quantity, price

order(price=10, item="Book", quantity=2)

def config(debug=False, version="1.0"):
    return debug, version

config(version="2.0", debug=True)
3️⃣ *args — Solutions
def sum_numbers(*args):
    return sum(args)

def max_value(*args):
    return max(args)

def print_all(*args):
    for v in args:
        print(v)

def average(*args):
    return sum(args) / len(args) if args else 0

def logger(*messages):
    for i, msg in enumerate(messages, 1):
        print(f"{i}. {msg}")
4️⃣ **kwargs — Solutions
def show_info(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

def build_user(**kwargs):
    return kwargs

def settings(**kwargs):
    return kwargs.get("debug", False)

def validate_user(**kwargs):
    if "name" not in kwargs or "email" not in kwargs:
        raise ValueError("Missing required fields")
    return True

def report(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
5️⃣ Lambda — Solutions
double = lambda x: x * 2
add = lambda a, b: a + b

names = ["Ali", "Peyman", "Arlette"]
sorted_names = sorted(names, key=lambda x: len(x))

nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))

values = [1, 2, 3]
squared = list(map(lambda x: x * x, values))
6️⃣ Scope — Solutions
def local_test():
    x = 10
    print(x)

y = 20
def global_test():
    print(y)

count = 0
def increment():
    global count
    count += 1

def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
7️⃣ Closures — Solutions
def simple_closure():
    x = 10
    def inner():
        return x
    return inner

def multiplier(n):
    return lambda x: x * n

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

def role_checker(role):
    def check(user_role):
        return user_role == role
    return check

def logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log
  
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161

