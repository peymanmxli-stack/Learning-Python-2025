1️⃣ Default Arguments — Examples

Default arguments provide safe defaults, reduce repetition, and make APIs easier to use.

# Example 1: Default greeting
def greet(name="User"):
    print(f"Hello, {name}")

greet()
greet("Peyman")

# Example 2: Default tax rate
def calculate_price(price, tax_rate=0.16):
    return price + (price * tax_rate)

print(calculate_price(100))
print(calculate_price(100, 0.08))

# Example 3: Logging function with default level
def log(message, level="INFO"):
    print(f"[{level}] {message}")

log("System started")
log("Disk space low", "WARNING")

# Example 4: File loader with default mode
def open_file(filename, mode="r"):
    return f"Opening {filename} in {mode} mode"

print(open_file("data.txt"))
print(open_file("data.txt", "w"))

2️⃣ Keyword Arguments — Examples

Keyword arguments improve clarity, readability, and flexibility.

# Example 1: Clear function call
def create_user(username, email, active=True):
    print(username, email, active)

create_user(username="peyman", email="p@email.com")

# Example 2: Reordering arguments safely
def connect(host, port, secure):
    print(host, port, secure)

connect(port=443, host="localhost", secure=True)

# Example 3: Optional configuration
def setup_app(debug=False, version="1.0"):
    print(debug, version)

setup_app(version="2.0", debug=True)

# Example 4: Readable API usage
def send_email(to, subject, body):
    print(to, subject)

send_email(
    subject="Welcome",
    body="Hello!",
    to="user@mail.com"
)

3️⃣ *args — Examples (Variable Positional Arguments)

Used when number of inputs is unknown.

# Example 1: Sum unlimited numbers
def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3))

# Example 2: Average calculator
def average(*values):
    return sum(values) / len(values)

print(average(10, 20, 30))

# Example 3: Print multiple messages
def log_messages(*messages):
    for msg in messages:
        print(msg)

log_messages("Start", "Loading", "Finished")

# Example 4: Combine strings
def join_words(*words):
    return " ".join(words)

print(join_words("Learning", "Python", "2025"))

4️⃣ **kwargs — Examples (Variable Keyword Arguments)

Used for dynamic, flexible data structures.

# Example 1: Display user info
def show_user(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_user(name="Peyman", age=43, country="Mexico")

# Example 2: Dynamic settings
def configure(**settings):
    print(settings)

configure(theme="dark", autosave=True)

# Example 3: HTML attributes simulation
def create_tag(**attrs):
    return attrs

print(create_tag(id="main", className="container"))

# Example 4: Flexible report generator
def generate_report(**data):
    for k, v in data.items():
        print(f"{k} -> {v}")

generate_report(cpu="80%", ram="16GB", os="Linux")

5️⃣ Lambda Functions — Examples

Used for short, one-line logic.

# Example 1: Square number
square = lambda x: x * x
print(square(5))

# Example 2: Add two values
add = lambda a, b: a + b
print(add(3, 4))

# Example 3: Sorting with lambda
names = ["Ali", "Peyman", "Arlette"]
names.sort(key=lambda x: len(x))
print(names)

# Example 4: Filter even numbers
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

6️⃣ Scope (LEGB Rule) — Examples

Scope controls where variables are accessible.

# Example 1: Local scope
def test():
    x = 10
    print(x)

test()

# Example 2: Global scope
x = 50

def show():
    print(x)

show()

# Example 3: Enclosing scope
def outer():
    y = 20
    def inner():
        print(y)
    inner()

outer()

# Example 4: Built-in scope
print(len([1, 2, 3]))

7️⃣ Closures — Examples

Closures remember values even after execution.

# Example 1: Simple closure
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print(double(5))

# Example 2: Counter
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())

# Example 3: Authorization check
def auth(role):
    def check(user_role):
        return user_role == role
    return check

is_admin = auth("admin")
print(is_admin("admin"))

# Example 4: Configured logger
def logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

error_log = logger("ERROR")
error_log("File not found")

👤 Author (ALWAYS)

Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
