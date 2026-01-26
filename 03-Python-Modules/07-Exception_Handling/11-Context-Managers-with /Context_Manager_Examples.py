# Example 1: File handling with context manager
with open("example.txt", "w") as file:
    file.write("Hello, Context Manager!")

# File is automatically closed here

# Example 2: Reading a file safely
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Example 3: Custom context manager
class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database connection")

with DatabaseConnection() as db:
    print("Using database")

# Example 4: Exception safety
try:
    with open("non_existing.txt", "r") as file:
        pass
except FileNotFoundError:
    print("Handled safely")
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
