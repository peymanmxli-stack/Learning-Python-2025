"""
🔄 Control Flow — while Loops
Professional Notes

A while loop executes code repeatedly while a condition is True.
The loop stops automatically when the condition becomes False.
"""


# ===========================================================================
# 🔹 1. Basic while Loop
# ===========================================================================

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# ===========================================================================
# 🔹 2. Infinite Loop (What NOT to Do)
# ===========================================================================

# ❌ This loop never stops
# while True:
#     print("Infinite loop")

# ✔ Always make sure there is a stopping condition


# ===========================================================================
# 🔹 3. Using break to Exit a Loop
# ===========================================================================

number = 1

while True:
    print(number)
    if number == 5:
        break
    number += 1


# ===========================================================================
# 🔹 4. Using continue to Skip Iterations
# ===========================================================================

num = 0

while num < 6:
    num += 1
    if num == 3:
        continue
    print("Current number:", num)


# ===========================================================================
# 🔹 5. while Loop with else
# ===========================================================================

x = 1

while x <= 3:
    print("x =", x)
    x += 1
else:
    print("Loop finished normally")


# ===========================================================================
# 🔹 6. User Input Loop
# ===========================================================================

# Keep asking until the user enters "exit"
# (Commented out to avoid blocking execution)

# user_input = ""
# while user_input != "exit":
#     user_input = input("Type 'exit' to quit: ")
#     print("You typed:", user_input)


# ===========================================================================
# 🔹 7. Using Flags
# ===========================================================================

running = True
counter = 0

while running:
    counter += 1
    print("Counter:", counter)

    if counter == 3:
        running = False


# ===========================================================================
# 🔹 8. Counting and Accumulation
# ===========================================================================

total = 0
i = 1

while i <= 5:
    total += i
    i += 1

print("Total:", total)


# ===========================================================================
# 🔹 9. Validation Example
# ===========================================================================

# Ensure positive number (example)
# value = int(input("Enter a positive number: "))
# while value <= 0:
#     print("Invalid input")
#     value = int(input("Enter a positive number: "))


# ===========================================================================
# 🔹 10. Common Mistakes
# ===========================================================================

# ❌ Forgetting to update the condition
# ❌ Overusing while instead of for
# ❌ Complex conditions that reduce clarity


# ===========================================================================
# ✅ Best Practices Summary
# ===========================================================================

# ✔ Always update loop variables
# ✔ Use break and continue intentionally
# ✔ Prefer flags for complex exit logic
# ✔ Keep conditions readable
# ✔ Use comments for clarity


# ===========================================================================
# 🧠 Summary
# ===========================================================================

# In this module, I learned:
# - How while loops work
# - When to use while vs for
# - How to prevent infinite loops
# - How to control flow using break and continue
# - How to write safe and readable while loops


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
