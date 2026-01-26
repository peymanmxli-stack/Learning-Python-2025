# Example 1: Simple assertion
age = 18
assert age >= 0

# Example 2: Assertion with message
temperature = -300
assert temperature >= -273.15, "Temperature below absolute zero!"

# Example 3: Assertion inside a function
def calculate_average(numbers):
    assert len(numbers) > 0, "List must not be empty"
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30]))

# Example 4: Assertion for internal logic
def withdraw(balance, amount):
    assert amount >= 0, "Withdrawal amount must be positive"
    assert balance >= amount, "Insufficient funds"
    return balance - amount

print(withdraw(1000, 250))
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
