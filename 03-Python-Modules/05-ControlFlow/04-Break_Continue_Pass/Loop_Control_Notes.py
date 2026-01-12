"""
⛔ Loop Control Statements — break / continue / pass
Professional Notes

Loop control statements allow us to alter the execution flow
inside for and while loops.
"""


# ===========================================================================
# 🔹 1. break — Exit the Loop Immediately
# ===========================================================================

for number in range(1, 10):
    if number == 5:
        break
    print(number)

# Output: 1 2 3 4


# ===========================================================================
# 🔹 2. break in while Loop
# ===========================================================================

count = 1

while True:
    print("Count:", count)
    if count == 3:
        break
    count += 1


# ===========================================================================
# 🔹 3. continue — Skip Current Iteration
# ===========================================================================

for number in range(1, 6):
    if number == 3:
        continue
    print("Number:", number)

# Output: 1 2 4 5


# ===========================================================================
# 🔹 4. continue in while Loop
# ===========================================================================

num = 0

while num < 5:
    num += 1
    if num == 2:
        continue
    print("Current:", num)


# ===========================================================================
# 🔹 5. pass — Placeholder Statement
# ===========================================================================

for i in range(3):
    pass  # To be implemented later

print("Loop finished")


# ===========================================================================
# 🔹 6. pass in Conditional Blocks
# ===========================================================================

value = 10

if value > 0:
    pass
else:
    print("Negative value")


# ===========================================================================
# 🔹 7. pass vs continue
# ===========================================================================

# pass does nothing
# continue skips to next iteration

for i in range(3):
    if i == 1:
        pass
    print("i =", i)

# Output: i = 0, i = 1, i = 2


# ===========================================================================
# 🔹 8. Real-World Example
# ===========================================================================

numbers = [10, -5, 0, 8, -2]

for n in numbers:
    if n < 0:
        continue
    if n == 0:
        break
    print("Valid number:", n)


# ===========================================================================
# ❌ Common Mistakes
# ===========================================================================

# ❌ Forgetting break in infinite loops
# ❌ Overusing continue
# ❌ Leaving pass in production code


# ===========================================================================
# ✅ Best Practices Summary
# ===========================================================================

# ✔ Use break for early exit
# ✔ Use continue to skip invalid cases
# ✔ Use pass only as a placeholder
# ✔ Keep control flow readable


# ===========================================================================
# 🧠 Summary
# ===========================================================================

# In this module, I learned:
# - How break stops loops
# - How continue skips iterations
# - Why pass exists and when to use it
# - How to control loop flow cleanly


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
