"""
Finally_Notes.py

Topic: Exception Handling — finally

This notes file explains the `finally` block in Python exception handling.
It is written as study notes, not runnable examples.

The goal is to understand HOW and WHY `finally` controls program flow.
"""

# ==================================================
# 1. What is `finally`?
# ==================================================
# `finally` is a block used with `try` (and optionally `except`).
# The code inside `finally` ALWAYS executes.
#
# It runs:
# - When no exception occurs
# - When an exception occurs
# - When an exception is handled
# - When an exception is NOT handled
# - Even when `return`, `break`, or `continue` is used


# ==================================================
# 2. Why `finally` is Important
# ==================================================
# In real programs, some actions MUST happen no matter what.
# These actions are usually called "cleanup".
#
# Common cleanup tasks:
# - Closing files
# - Closing database connections
# - Releasing system resources
# - Unlocking files or threads
# - Logging program completion
#
# `finally` guarantees that cleanup code runs.


# ==================================================
# 3. Basic Structure
# ==================================================
# try:
#     code_that_may_fail
# except SomeError:
#     handle_the_error
# finally:
#     cleanup_code


# ==================================================
# 4. `finally` Without `except`
# ==================================================
# `finally` can be used without an `except` block.
# This is useful when you don't want to handle errors,
# but still want guaranteed cleanup.
#
# try:
#     risky_operation
# finally:
#     cleanup


# ==================================================
# 5. Execution Order
# ==================================================
# Python always follows this order:
#
# 1. Enter try block
# 2. If exception occurs → go to except (if exists)
# 3. Execute finally block
# 4. Continue program OR crash (if exception unhandled)
#
# IMPORTANT:
# `finally` runs BEFORE the program exits or crashes.


# ==================================================
# 6. `finally` and return
# ==================================================
# If a `return` statement appears in `try` or `except`,
# Python still executes `finally` before returning.
#
# This means `finally` can NOT be skipped.


# ==================================================
# 7. `finally` and loops
# ==================================================
# When used inside loops:
# - `break` does NOT skip `finally`
# - `continue` does NOT skip `finally`
#
# `finally` executes before the loop exits or continues.


# ==================================================
# 8. `finally` vs `else`
# ==================================================
# try / except / else / finally
#
# - `else` runs ONLY if no exception occurs
# - `finally` runs ALWAYS
#
# `else` is for normal logic
# `finally` is for cleanup logic


# ==================================================
# 9. `finally` and `with`
# ==================================================
# The `with` statement internally uses try/finally.
#
# Example concept:
#
# with open("file.txt") as f:
#     data = f.read()
#
# Is equivalent to:
#
# f = open("file.txt")
# try:
#     data = f.read()
# finally:
#     f.close()


# ==================================================
# 10. Best Practices
# ==================================================
# ✅ Use `finally` ONLY for cleanup tasks
# ✅ Keep `finally` blocks short and safe
# ❌ Do not place complex logic in `finally`
# ❌ Avoid raising new exceptions inside `finally`


# ==================================================
# 11. Key Takeaway
# ==================================================
# `finally` is a GUARANTEED execution block.
# If you need code that must run no matter what — use `finally`.


# ==================================================
# End of Finally_Notes.py
# ==================================================
# ===========================================================================
# 👤 Author
# ===========================================================================
👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
🏁 End of Examples
