"""
PYTHON COLLECTIONS — COMPLETE THEORY & PROFESSIONAL NOTES

This file provides a deep, structured, and professional explanation of
Python collections. These data structures are fundamental to writing
efficient, readable, and scalable Python programs.

Collections are used everywhere:
- Software systems
- Data processing
- APIs and web applications
- Game development
- Automation and scripting
- Configuration management
"""

# ==========================================================
# 1️⃣ LIST
# ==========================================================

"""
WHAT IS A LIST?
A list is an ordered, mutable collection of elements.
Elements can be of any data type and can be mixed.

WHY LISTS EXIST
Lists exist to store sequences of data that may:
- Change over time
- Grow or shrink dynamically
- Require ordering and indexing

WHY WE USE LISTS
- To store multiple values in a single variable
- To loop over data
- To collect user input
- To manage results, logs, queues, stacks

WHEN TO USE LISTS
- When order matters
- When data will change
- When duplicates are allowed

KEY CHARACTERISTICS
✔ Ordered
✔ Mutable (can be changed)
✔ Allows duplicates
✔ Indexed (0-based)

COMMON LIST OPERATIONS
- append()
- insert()
- remove()
- pop()
- sort()
- reverse()

COMMON MISTAKES
✘ Modifying a list while iterating over it
✘ Using lists when a set would be faster
✘ Forgetting lists are mutable

BEST PRACTICES
✔ Use list comprehensions for clarity
✔ Keep lists homogeneous when possible
✔ Avoid very large lists when sets/dicts are better
"""

# ==========================================================
# 2️⃣ TUPLE
# ==========================================================

"""
WHAT IS A TUPLE?
A tuple is an ordered, immutable collection of elements.

WHY TUPLES EXIST
Tuples exist to store data that should NOT change.
They provide data safety and performance benefits.

WHY WE USE TUPLES
- Protect data from accidental modification
- Represent fixed structures
- Use as dictionary keys
- Improve performance in read-only data

WHEN TO USE TUPLES
- Coordinates (x, y)
- Configuration values
- Function return values
- Records that must not change

KEY CHARACTERISTICS
✔ Ordered
✔ Immutable
✔ Allows duplicates
✔ Faster than lists

COMMON TUPLE OPERATIONS
- Indexing
- Unpacking
- Iteration

COMMON MISTAKES
✘ Trying to modify tuple values
✘ Using tuple where data must change

BEST PRACTICES
✔ Use tuples for constants
✔ Use unpacking for readability
✔ Prefer tuple over list for fixed data
"""

# ==========================================================
# 3️⃣ SET
# ==========================================================

"""
WHAT IS A SET?
A set is an unordered collection of unique elements.

WHY SETS EXIST
Sets exist to efficiently:
- Remove duplicates
- Test membership
- Perform mathematical set operations

WHY WE USE SETS
- Fast lookup (O(1))
- Automatically removes duplicates
- Clean mathematical logic

WHEN TO USE SETS
- Ensuring uniqueness
- Comparing datasets
- Finding intersections or differences

KEY CHARACTERISTICS
✔ Unordered
✔ Mutable
✔ No duplicates
✔ Very fast membership tests

COMMON SET OPERATIONS
- add()
- remove()
- union()
- intersection()
- difference()

COMMON MISTAKES
✘ Expecting order
✘ Using sets when order matters

BEST PRACTICES
✔ Convert lists to sets to remove duplicates
✔ Use set operations instead of loops
✔ Use frozenset for immutable sets
"""

# ==========================================================
# 4️⃣ DICTIONARY
# ==========================================================

"""
WHAT IS A DICTIONARY?
A dictionary stores data as key-value pairs.

WHY DICTIONARIES EXIST
Dictionaries exist to allow:
- Fast data retrieval
- Structured data storage
- Named data access

WHY WE USE DICTIONARIES
- Configuration files
- JSON-like data
- Database records
- User profiles

WHEN TO USE DICTIONARIES
- When data has meaning (keys)
- When fast lookup is needed
- When mapping relationships

KEY CHARACTERISTICS
✔ Mutable
✔ Keys must be unique
✔ Values can be any type
✔ Extremely fast lookup

COMMON DICTIONARY OPERATIONS
- get()
- keys()
- values()
- items()
- update()
- pop()

COMMON MISTAKES
✘ Accessing missing keys directly
✘ Using mutable keys
✘ Overcomplicating with nested dicts

BEST PRACTICES
✔ Use .get() to avoid KeyError
✔ Keep keys simple and consistent
✔ Validate dictionary data
"""

# ==========================================================
# 5️⃣ NESTED COLLECTIONS
# ==========================================================

"""
WHAT ARE NESTED COLLECTIONS?
Collections that contain other collections.

WHY THEY EXIST
To model complex, real-world data structures.

WHY WE USE THEM
- Represent users, products, systems
- Work with JSON and APIs
- Build complex data models

WHEN TO USE NESTED COLLECTIONS
- Structured datasets
- Hierarchical information
- Configuration schemas

COMMON MISTAKES
✘ Deep nesting without structure
✘ Poor readability
✘ Hard-coded indexes

BEST PRACTICES
✔ Keep nesting shallow when possible
✔ Use clear keys
✔ Validate data carefully
"""

# ==========================================================
# 6️⃣ MUTABILITY VS IMMUTABILITY
# ==========================================================

"""
MUTABLE COLLECTIONS
- List
- Set
- Dictionary

IMMUTABLE COLLECTIONS
- Tuple
- Frozenset

WHY THIS MATTERS
Mutability affects:
- Function behavior
- Memory safety
- Debugging difficulty

BEST PRACTICES
✔ Prefer immutability when possible
✔ Avoid modifying shared objects
✔ Be explicit when mutating data
"""

# ==========================================================
# 7️⃣ PERFORMANCE CONSIDERATIONS
# ==========================================================

"""
TIME COMPLEXITY OVERVIEW
- List lookup: O(n)
- Set lookup: O(1)
- Dict lookup: O(1)

WHY PERFORMANCE MATTERS
- Large datasets
- Real-time systems
- Scalable applications

BEST PRACTICES
✔ Use dict/set for lookups
✔ Avoid unnecessary loops
✔ Choose the right structure early
"""

# ==========================================================
# 8️⃣ PROFESSIONAL BEST PRACTICES SUMMARY
# ==========================================================

"""
✔ Use LIST when order & mutability matter
✔ Use TUPLE for fixed, protected data
✔ Use SET for uniqueness & comparisons
✔ Use DICTIONARY for structured records
✔ Avoid over-nesting
✔ Write readable, maintainable code
"""

# ==========================================================
# 👤 Author
# ==========================================================

"""
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
"""
