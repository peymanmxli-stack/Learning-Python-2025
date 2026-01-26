"""
====================================================
ERROR HANDLING — try / except
THEORY & PROFESSIONAL NOTES
====================================================

This file provides a deep, structured, and professional
explanation of error handling in Python.

Error handling allows programs to detect, manage,
and recover from runtime errors without crashing.
"""

# ====================================================
# 1. WHAT IS AN ERROR?
# ====================================================
"""
An error is a problem that occurs during program execution
that interrupts the normal flow of a program.

Errors can happen due to:
• Invalid user input
• Missing files
• Network failures
• Logical mistakes
• Unexpected conditions

Without error handling, Python stops execution immediately.
"""

# ====================================================
# 2. ERROR VS EXCEPTION
# ====================================================
"""
In Python, most runtime errors are called EXCEPTIONS.

Error (general concept):
- Something went wrong

Exception (Python-specific):
- A runtime error object raised by Python

Examples of common exceptions:
• ZeroDivisionError
• ValueError
• TypeError
• FileNotFoundError
• IndexError
"""

# ====================================================
# 3. WHY ERROR HANDLING IS NECESSARY
# ====================================================
"""
Professional software must never crash unexpectedly.

Error handling allows programs to:
✔ Fail safely
✔ Continue running
✔ Show friendly error messages
✔ Protect data
✔ Improve user experience

Error handling is essential for:
• User-facing applications
• Servers and APIs
• Automation scripts
• Financial and security systems
"""

# ====================================================
# 4. THE try / except STRUCTURE
# ====================================================
"""
The try / except block is used to catch exceptions.

Basic structure:

try:
    # code that may fail
except:
    # code that runs if an error occurs

If an error happens inside try:
- Python jumps immediately to except
- Program does NOT crash
"""

# ====================================================
# 5. HOW try / except WORKS INTERNALLY
# ====================================================
"""
Execution flow:

1️⃣ Python enters try block
2️⃣ If no error occurs → skip except
3️⃣ If an error occurs → jump to except
4️⃣ Program continues after the block

Important:
• Only errors inside try are caught
• Errors outside still crash the program
"""

# ====================================================
# 6. HANDLING SPECIFIC EXCEPTIONS
# ====================================================
"""
Catching specific exceptions is best practice.

Why?
✔ Better control
✔ Clear intent
✔ Safer code

Example exceptions:
• ValueError → invalid conversion
• ZeroDivisionError → divide by zero
• TypeError → wrong data type
"""

# ====================================================
# 7. MULTIPLE except BLOCKS
# ====================================================
"""
A try block can have multiple except blocks.

Python checks them from top to bottom.
The first matching exception is executed.

This allows precise error handling.
"""

# ====================================================
# 8. THE else BLOCK
# ====================================================
"""
The else block runs ONLY if:
✔ No exception occurred

Structure:

try:
    risky code
except:
    handle error
else:
    run if no error

Purpose:
✔ Separate success logic from error logic
✔ Improve readability
"""

# ====================================================
# 9. THE finally BLOCK
# ====================================================
"""
The finally block ALWAYS runs.

It executes:
✔ Whether an error occurred or not
✔ Even if return is used

Used for:
• Closing files
• Releasing resources
• Database cleanup
• Network disconnections
"""

# ====================================================
# 10. COMMON BUILT-IN EXCEPTIONS
# ====================================================
"""
Some frequently used exceptions:

• ValueError        → invalid value
• TypeError         → wrong data type
• ZeroDivisionError → division by zero
• IndexError        → invalid index
• KeyError          → missing dictionary key
• FileNotFoundError → file does not exist
• ImportError       → module not found
"""

# ====================================================
# 11. THE Exception BASE CLASS
# ====================================================
"""
All Python exceptions inherit from the Exception class.

Catching Exception catches:
✔ All standard exceptions

⚠️ Avoid using it unless necessary
because it can hide bugs.
"""

# ====================================================
# 12. RAISING EXCEPTIONS
# ====================================================
"""
Python allows raising exceptions manually.

Why raise exceptions?
✔ Enforce rules
✔ Validate input
✔ Stop execution intentionally

Use raise when a condition should NEVER be allowed.
"""

# ====================================================
# 13. CUSTOM EXCEPTIONS
# ====================================================
"""
Custom exceptions allow:
✔ Clear domain-specific errors
✔ Better debugging
✔ Cleaner code

They are created by subclassing Exception.
"""

# ====================================================
# 14. ERROR HANDLING VS VALIDATION
# ====================================================
"""
Validation:
✔ Prevents errors before they happen

Error handling:
✔ Catches errors after they happen

Professional code uses BOTH.
"""

# ====================================================
# 15. COMMON BEGINNER MISTAKES
# ====================================================
"""
❌ Using bare except
❌ Swallowing errors silently
❌ Mixing print and logic
❌ Using exceptions for normal flow
❌ Not handling user input
"""

# ====================================================
# 16. BEST PRACTICES FOR ERROR HANDLING
# ====================================================
"""
✔ Catch specific exceptions
✔ Keep try blocks small
✔ Never ignore exceptions
✔ Use finally for cleanup
✔ Provide meaningful messages
✔ Do not overuse exceptions
✔ Write readable error-handling code
"""

# ====================================================
# END OF NOTES — ERROR HANDLING
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
