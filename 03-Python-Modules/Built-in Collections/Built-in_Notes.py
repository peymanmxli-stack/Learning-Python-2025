"""
====================================================
PYTHON BUILT-IN COLLECTIONS
THEORY & PROFESSIONAL NOTES
====================================================

This file provides a complete, structured, and professional
explanation of Python’s core built-in collection types.

These collections are fundamental tools used to store,
organize, and manage multiple values efficiently in
real-world Python applications.

Collections covered in this file:
- list
- tuple
- str
- range
- set
"""

# ====================================================
# 1. WHAT ARE BUILT-IN COLLECTIONS?
# ====================================================
"""
Built-in collections are data structures provided by Python
to store multiple values inside a single variable.

Instead of creating many separate variables, collections
allow us to group related data logically and efficiently.

Collections help us:
✔ Organize data
✔ Reduce code repetition
✔ Improve readability
✔ Build scalable programs
"""

# ====================================================
# 2. LISTS
# ====================================================
"""
WHAT IS A LIST?
A list is an ordered, mutable collection of items.

- Ordered → items have a position (index)
- Mutable → items can be changed after creation
- Allows duplicate values

WHY WE USE LISTS:
✔ Store sequences of data
✔ Modify data dynamically
✔ Collect user input
✔ Process data step by step

Lists are one of the most commonly used data structures
in Python.
"""

numbers = [10, 20, 30, 40]
names = ["Peyman", "Arlette", "Carlos"]

# ====================================================
# 3. TUPLES
# ====================================================
"""
WHAT IS A TUPLE?
A tuple is an ordered, immutable collection of items.

- Ordered → items have an index
- Immutable → cannot be modified after creation
- Allows duplicate values

WHY WE USE TUPLES:
✔ Protect data from accidental changes
✔ Represent fixed records
✔ Improve performance
✔ Use as dictionary keys

Tuples are used when data must remain constant.
"""

coordinates = (10, 20)
user_profile = ("Peyman", 43, "IT Engineering")

# ====================================================
# 4. STRINGS
# ====================================================
"""
WHAT IS A STRING?
A string is an immutable sequence of characters.

Although often treated as text, strings are actually
a built-in sequence type in Python.

WHY WE USE STRINGS:
✔ Store text data
✔ Handle user input
✔ Process messages, files, and logs
✔ Communicate with users and systems

Strings behave like sequences and support indexing
and iteration.
"""

message = "Welcome to Python"
username = "admin_user"

# ====================================================
# 5. RANGE
# ====================================================
"""
WHAT IS RANGE?
The range type represents an immutable sequence of numbers.

It does NOT store all numbers in memory.
Instead, it generates numbers when needed.

WHY WE USE RANGE:
✔ Efficient looping
✔ Memory optimization
✔ Generate numeric sequences
✔ Control iteration flow

Range is commonly used with loops.
"""

numbers_range = range(1, 6)

# ====================================================
# 6. SETS
# ====================================================
"""
WHAT IS A SET?
A set is an unordered collection of unique elements.

- Unordered → no index positions
- No duplicates allowed
- Mutable (set) or immutable (frozenset)

WHY WE USE SETS:
✔ Remove duplicate values
✔ Fast membership testing
✔ Perform set operations
✔ Compare collections

Sets are ideal for uniqueness and validation.
"""

unique_numbers = {1, 2, 3, 4}
skills = {"Python", "Networking", "Security"}

# ====================================================
# 7. COMPARISON SUMMARY
# ====================================================
"""
COLLECTION TYPE COMPARISON:

list:
- Ordered
- Mutable
- Allows duplicates

tuple:
- Ordered
- Immutable
- Allows duplicates

str:
- Ordered
- Immutable
- Sequence of characters

range:
- Ordered
- Immutable
- Numeric sequence generator

set:
- Unordered
- Mutable
- No duplicates

Choosing the correct collection type is a key
professional programming skill.
"""

# ====================================================
# 8. WHY COLLECTION CHOICE MATTERS
# ====================================================
"""
In professional software development:

✔ The wrong collection can cause bugs
✔ The right collection improves performance
✔ Clean data structures improve readability
✔ Scalable systems depend on correct data modeling

Professional developers think in terms of
DATA STRUCTURES, not just variables.
"""

# ====================================================
# 9. BEST PRACTICES
# ====================================================
"""
✔ Use lists for changeable sequences
✔ Use tuples for fixed data
✔ Treat strings as sequences, not just text
✔ Use range for loops instead of manual counters
✔ Use sets for uniqueness and validation
✔ Keep data structures simple and readable
"""

# ====================================================
# END OF NOTES — BUILT-IN COLLECTIONS
# ====================================================

"""
Next Topics:
- LISTS — Detailed Notes, Examples, Tasks
- TUPLES — Detailed Notes, Examples, Tasks
- STRINGS — Detailed Notes, Examples, Tasks
- RANGE — Detailed Notes, Examples, Tasks
- SETS — Detailed Notes, Examples, Tasks
"""

👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
