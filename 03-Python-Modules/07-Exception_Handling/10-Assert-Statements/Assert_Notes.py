"""
ASSERT STATEMENTS — THEORY & NOTES

The assert statement checks whether a condition is True.
If the condition is False, Python raises an AssertionError.

Syntax:
assert condition
assert condition, "Error message"

Assertions are used for:
- Debugging
- Validating internal logic
- Catching programmer mistakes

They should NOT be used for:
- User input validation
- Runtime error handling
- Production-critical logic

Assertions can be disabled using:
python -O script.py
"""

# Example structure
x = 10
assert x > 0

# With custom message
y = -5
assert y >= 0, "y must be non-negative"
Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
