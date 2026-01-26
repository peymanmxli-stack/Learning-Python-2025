"""
CONTEXT MANAGERS — THEORY & NOTES

A context manager is an object that defines:
- __enter__()
- __exit__()

It is used with the 'with' statement.

Basic syntax:
with resource as variable:
    block

The resource is automatically cleaned up when the block ends,
even if an exception occurs.

Equivalent try/finally:
try:
    resource = open("file.txt")
finally:
    resource.close()
"""

# Example explanation
class SimpleContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        return False  # Do not suppress exceptions
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
