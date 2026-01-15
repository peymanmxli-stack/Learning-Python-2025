"""
Finally_Tasks_Solutions.py

Topic: Exception Handling — finally

This file contains complete and correct solutions for:
Finally_Tasks.py (Rank 1 → Rank 5)

Each solution is clearly separated and commented.
Compare your answers carefully and understand WHY `finally` executes.
"""

# ==================================================
# Rank 1 — Solution
# ==================================================
print("\nRank 1 — Solution")
try:
    print("Start")
finally:
    print("End")


# ==================================================
# Rank 2 — Solution
# ==================================================
print("\nRank 2 — Solution")
try:
    a = 10
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Operation finished")


# ==================================================
# Rank 3 — Solution
# ==================================================
print("\nRank 3 — Solution")

def calculate():
    try:
        return 100
    finally:
        print("Cleanup before return")

print("Returned value:", calculate())


# ==================================================
# Rank 4 — Solution
# ==================================================
print("\nRank 4 — Solution")
for i in range(5):
    try:
        print("Loop value:", i)
        if i == 2:
            break
    finally:
        print("Loop cleanup")


# ==================================================
# Rank 5 — Solution
# ==================================================
print("\nRank 5 — Solution")

file = None
try:
    file = open("task_file.txt", "w")
    file.write("This file is safely handled using finally.\n")
    print("File written successfully")

    # Intentional error
    x = 10 / 0

except ZeroDivisionError:
    print("Intentional error occurred")

finally:
    if file:
        file.close()
        print("File closed safely (finally executed)")


# ==================================================
# End of Finally_Tasks_Solutions.py
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
# ==================================================
