"""
📘 Module — Basic Data Types: String (str)
📂 Examples File

This file contains small, focused demonstrations of how strings work
in Python. Each example illustrates a common concept or real use case.

▶ Run this file directly:
    python String_Examples.py
"""


# ===========================================================================
# 🟢 Rank 1 — Basic string creation and printing
# ===========================================================================

def example_1_string_creation():
    """Show simple string creation and printing."""
    print("Example 1 — String creation")
    a = "Hello"
    b = 'World'
    c = """Multi-line
string example."""
    print(a, b)
    print(c)
    print()


def example_2_concatenation_and_length():
    """Demonstrate concatenation and length of strings."""
    print("Example 2 — Concatenation & length")
    text = "Python" + " " + "Rocks"
    print(text)
    print("Length:", len(text))
    print()


# ===========================================================================
# 🔵 Rank 2 — Indexing, slicing, and methods
# ===========================================================================

def example_3_indexing_and_slicing():
    """Show indexing and slicing operations."""
    print("Example 3 — Indexing & slicing")
    s = "Programming"
    print(s[0])     # first char
    print(s[-1])    # last char
    print(s[0:6])   # "Progra"
    print(s[::-1])  # reversed
    print()


def example_4_basic_methods():
    """Demonstrate common string methods."""
    print("Example 4 — Common string methods")
    s = "  Python Programming  "
    print("Original:", repr(s))
    print("lower():", s.lower())
    print("upper():", s.upper())
    print("strip():", s.strip())
    print("replace():", s.replace("Python", "Java"))
    print("split():", s.split())
    print()


# ===========================================================================
# 🟡 Rank 3 — Formatting, loops, searching
# ===========================================================================

def example_5_fstring_formatting():
    """Show f-string formatting."""
    print("Example 5 — f-strings")
    name = "Peyman"
    score = 95
    print(f"Student {name} scored {score} points.")
    print(f"Formatted number: {3.14159:.3f}")
    print()


def example_6_looping_over_strings():
    """Loop over characters in a string."""
    print("Example 6 — Looping over a string")
    word = "Nova"
    for ch in word:
        print("Character:", ch)
    print()


def example_7_search_and_count():
    """Demonstrate counting and searching."""
    print("Example 7 — Searching & counting")
    t = "banana"
    print("Count 'a':", t.count("a"))
    print("First 'na':", t.find("na"))
    print("'na' in text?", "na" in t)
    print()


# ===========================================================================
# 🟠 Rank 4 — Realistic string processing
# ===========================================================================

def example_8_clean_and_normalize_text():
    """Clean and normalize user input text."""
    print("Example 8 — Cleaning text")
    raw = "   Hello PYTHON   "
    cleaned = raw.strip().lower()
    print("Raw:", repr(raw))
    print("Cleaned:", repr(cleaned))
    print()


def example_9_joining_strings():
    """Join a list of strings into a single message."""
    print("Example 9 — Joining")
    parts = ["Hello", "from", "Nova"]
    result = " ".join(parts)
    print(result)
    print()


# ===========================================================================
# 🔴 Rank 5 — Professional patterns
# ===========================================================================

def example_10_building_dynamic_messages():
    """Build a dynamic message using f-strings."""
    print("Example 10 — Dynamic messages")
    user = "Peyman"
    action = "completed Module 18"
    msg = f"✨ {user} has {action}! Great work!"
    print(msg)
    print()


def example_11_simple_parser():
    """Parse a CSV-style string."""
    print("Example 11 — Simple parser")
    line = "Peyman,43,Mexicali,IT Engineering"
    parts = line.split(",")
    name, age, city, field = parts
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Field:", field)
    print()


def example_12_masking_sensitive_info():
    """Mask part of a string (real-world scenario)."""
    print("Example 12 — Masking sensitive info")
    email = "peyman@example.com"
    masked = email[:3] + "***" + email[-10:]
    print("Original:", email)
    print("Masked:  ", masked)
    print()


# ===========================================================================
# ▶ Main entry point
# ===========================================================================

def main():
    """Run all examples in order."""

    # Rank 1
    example_1_string_creation()
    example_2_concatenation_and_length()

    # Rank 2
    example_3_indexing_and_slicing()
    example_4_basic_methods()

    # Rank 3
    example_5_fstring_formatting()
    example_6_looping_over_strings()
    example_7_search_and_count()

    # Rank 4
    example_8_clean_and_normalize_text()
    example_9_joining_strings()

    # Rank 5
    example_10_building_dynamic_messages()
    example_11_simple_parser()
    example_12_masking_sensitive_info()


if __name__ == "__main__":
    main()

# ===========================================================================
# 👤 Author
# ===========================================================================
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2025
🆔 ID: 250161

# 🏁 End of Notes
