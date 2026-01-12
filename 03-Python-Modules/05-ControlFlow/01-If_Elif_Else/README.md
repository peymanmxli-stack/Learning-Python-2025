# 🔀 Control Flow — if / elif / else

## ✨ Overview

The `if / elif / else` structure is the foundation of **decision-making** in Python.
It allows a program to **choose different execution paths** based on conditions.

This construct is used everywhere:
- Validating user input
- Controlling program logic
- Handling business rules
- Managing permissions and states
- Reacting to real-time data

Understanding conditional logic clearly is essential for writing **correct,
readable, and maintainable Python code**.

---

## 🎯 Learning Objectives

By studying this section, I will be able to:

- Use `if`, `elif`, and `else` to control execution flow
- Write clear boolean expressions
- Combine conditions using logical operators
- Avoid common conditional mistakes
- Structure readable decision trees
- Apply best practices for clean conditional logic

---

## 🧠 Concept: How Python Evaluates Conditions

Python evaluates conditions **top to bottom**:

1. The `if` condition is checked first
2. If it is `True`, its block runs and the rest are skipped
3. If `False`, Python checks each `elif`
4. If none match, the `else` block runs (if present)

Only **one branch executes**.

---

## 🔹 Basic Syntax

```python
if condition:
    # code runs if condition is True
elif another_condition:
    # runs if previous conditions were False
else:
    # runs if all conditions were False

🔢 Comparison Operators

Used to compare values:

Operator	Meaning
==	equal to
!=	not equal to
<	less than
>	greater than
<=	less than or equal
>=	greater than or equal

Example:

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
🔗 Logical Operators

Used to combine conditions:

Operator	Meaning
and	all conditions must be True
or	at least one condition is True
not	negates the condition

Example:

age = 25
has_id = True

if age >= 18 and has_id:
    print("Access granted")

🧩 Using elif Effectively

Use elif to avoid deeply nested if statements.

❌ Less readable:

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")


✅ Better:

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
⚠️ Common Mistakes
❌ Using assignment instead of comparison
if x = 5:   # ERROR

❌ Overusing else

Sometimes no else is needed.

if value < 0:
    print("Negative")

✅ Best Practices

✔ Keep conditions simple and readable
✔ Avoid deeply nested if blocks
✔ Use meaningful variable names
✔ Prefer elif over nested if
✔ Use early returns inside functions
✔ Write conditions that express intent clearly

📁 Suggested Files for This Section
If_Elif_Else/
├── README.md
├── If_Elif_Else_Notes.py
├── If_Elif_Else_Examples.py
├── If_Elif_Else_Tasks.py
└── If_Elif_Else_Tasks_Solutions.py

🧠 Summary

In this section, I learned:

How conditional branching works in Python

How Python evaluates conditions

How to write clean decision logic

How to avoid common conditional pitfalls

How to structure readable control flow

This knowledge is a core foundation for all advanced Python topics.

👤 Author

👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
