"""
ADVANCED FUNCTIONS — THEORY & NOTES

1. Default Arguments
Functions can have default values for parameters.

2. Keyword Arguments
Arguments passed by name increase readability.

3. *args
Allows passing a variable number of positional arguments.

4. **kwargs
Allows passing a variable number of keyword arguments.

5. Lambda Functions
Small anonymous functions.

6. Scope
Local, global, enclosing, built-in (LEGB rule).

7. Closures
Functions that remember values from their enclosing scope.
"""

# Default arguments
def greet(name="User"):
    print(f"Hello, {name}")

# *args
def add_numbers(*numbers):
    return sum(numbers)

# **kwargs
def print_info(**info):
    for key, value in info.items():
        print(key, value)

# Lambda
square = lambda x: x * x

👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
