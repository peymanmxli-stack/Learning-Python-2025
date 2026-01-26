# Rank 1
number = 5
assert number > 0

# Rank 2
text = "Python"
assert len(text) > 0

# Rank 3
def first_element(lst):
    assert len(lst) > 0, "List cannot be empty"
    return lst[0]

# Rank 4
def divide(a, b):
    assert b != 0, "Divider must not be zero"
    assert isinstance(a, (int, float))
    assert isinstance(b, (int, float))
    return a / b

# Rank 5
def process_score(score):
    assert 0 <= score <= 100, "Score must be between 0 and 100"
    if score >= 60:
        return "Pass"
    return "Fail"
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
