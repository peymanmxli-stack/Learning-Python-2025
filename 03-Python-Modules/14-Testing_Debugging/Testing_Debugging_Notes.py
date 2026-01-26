"""
====================================================
TESTING & DEBUGGING — NOTES (DEEP THEORY)
====================================================

This file contains a complete and professional
theoretical explanation of Testing & Debugging
in Python.

Focus:
✔ Understanding bugs
✔ Preventing errors
✔ Writing reliable code
✔ Debugging like a professional
"""

# ====================================================
# 1️⃣ WHAT IS A BUG?
# ====================================================

"""
A bug is an error, flaw, or mistake in a program
that causes it to behave incorrectly or unexpectedly.

Bugs can cause:
• Program crashes
• Wrong outputs
• Security vulnerabilities
• Performance issues

Bugs are a normal part of programming — even
experienced developers write buggy code.
"""


# ====================================================
# 2️⃣ WHY BUGS HAPPEN
# ====================================================

"""
Common reasons bugs occur:

1️⃣ Human error (logic mistakes)
2️⃣ Incorrect assumptions
3️⃣ Edge cases not considered
4️⃣ Typing mistakes
5️⃣ Misunderstanding requirements
6️⃣ Changes to existing code

Testing and debugging exist to CONTROL bugs,
not eliminate human imperfection.
"""


# ====================================================
# 3️⃣ TYPES OF ERRORS IN PYTHON
# ====================================================

"""
Python errors are generally divided into three types:
"""

# ----------------------------------------------------
# 🔹 Syntax Errors
# ----------------------------------------------------

"""
Syntax errors occur when Python cannot understand
the code structure.

Examples:
• Missing colon
• Incorrect indentation
• Misspelled keywords

These errors are caught BEFORE the program runs.
"""

# ----------------------------------------------------
# 🔹 Runtime Errors (Exceptions)
# ----------------------------------------------------

"""
Runtime errors occur while the program is running.

Examples:
• ZeroDivisionError
• TypeError
• ValueError
• IndexError
• KeyError

These errors crash the program unless handled.
"""

# ----------------------------------------------------
# 🔹 Logic Errors
# ----------------------------------------------------

"""
Logic errors occur when the program runs without
crashing but produces incorrect results.

These are the MOST dangerous bugs because:
❌ No error message
❌ Harder to detect
❌ Require testing to find
"""


# ====================================================
# 4️⃣ WHAT IS TESTING?
# ====================================================

"""
Testing is the process of verifying that a program
produces correct results under expected and
unexpected conditions.

Testing answers the question:
"Does my code do what it is supposed to do?"
"""

# ====================================================
# 5️⃣ WHY WE TEST CODE
# ====================================================

"""
Testing helps to:
✔ Detect bugs early
✔ Prevent regressions
✔ Improve code quality
✔ Increase confidence
✔ Reduce future costs
✔ Support teamwork

In professional development, untested code
is considered incomplete.
"""


# ====================================================
# 6️⃣ TYPES OF TESTING
# ====================================================

# ----------------------------------------------------
# 🔹 Manual Testing
# ----------------------------------------------------

"""
Manual testing is when the developer runs the program
and checks results by hand.

Pros:
✔ Simple
✔ No tools needed

Cons:
❌ Slow
❌ Error-prone
❌ Not scalable
"""

# ----------------------------------------------------
# 🔹 Automated Testing
# ----------------------------------------------------

"""
Automated testing uses code to test code.

Pros:
✔ Fast
✔ Repeatable
✔ Reliable
✔ Scalable

This is the professional standard.
"""


# ====================================================
# 7️⃣ WHAT IS DEBUGGING?
# ====================================================

"""
Debugging is the systematic process of:
1️⃣ Identifying a bug
2️⃣ Understanding why it happens
3️⃣ Fixing the root cause

Debugging is NOT guessing.
It is logical investigation.
"""


# ====================================================
# 8️⃣ DEBUGGING TECHNIQUES
# ====================================================

# ----------------------------------------------------
# 🔹 Print Debugging
# ----------------------------------------------------

"""
Using print() statements to inspect variable values
and execution flow.

Pros:
✔ Simple
✔ Quick

Cons:
❌ Messy
❌ Not scalable
"""

# ----------------------------------------------------
# 🔹 Step-by-Step Debugging
# ----------------------------------------------------

"""
Following program execution line by line,
observing variable changes.

This helps isolate where logic breaks.
"""

# ----------------------------------------------------
# 🔹 Using a Debugger
# ----------------------------------------------------

"""
Debuggers allow you to:
✔ Pause execution
✔ Inspect variables
✔ Step through code
✔ Set breakpoints

Professional IDEs provide built-in debuggers.
"""


# ====================================================
# 9️⃣ ASSERTIONS
# ====================================================

"""
Assertions are checks that ensure conditions
are true during execution.

If an assertion fails:
❌ Program stops
❌ Error message appears

Assertions are used to:
✔ Catch bugs early
✔ Validate assumptions
✔ Improve code reliability
"""


# ====================================================
# 🔟 WRITING TESTABLE CODE
# ====================================================

"""
Good code is easy to test.

Principles:
✔ Small functions
✔ Clear logic
✔ Predictable behavior
✔ Avoid hard-coded values
✔ Use meaningful names

Testable code = maintainable code.
"""


# ====================================================
# 1️⃣1️⃣ DEBUGGING MINDSET
# ====================================================

"""
Professional debugging mindset:

✔ Stay calm
✔ Reproduce the bug
✔ Isolate the problem
✔ Understand before fixing
✔ Verify the fix
✔ Prevent regression

Debugging is a skill developed through practice.
"""


# ====================================================
# 1️⃣2️⃣ BEST PRACTICES
# ====================================================

"""
✔ Test early and often
✔ Never assume code works
✔ Write clear error messages
✔ Handle exceptions properly
✔ Keep debugging tools ready
✔ Learn from every bug

In real-world software:
Testing is not optional.
"""


# ====================================================
# END OF NOTES — TESTING & DEBUGGING
# ====================================================

"""
Next File:
Testing_Debugging_Examples.py
"""

# ====================================================
# 👤 Author Information
# ====================================================

"""
👤 Author: Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 Student ID: 250161
"""
