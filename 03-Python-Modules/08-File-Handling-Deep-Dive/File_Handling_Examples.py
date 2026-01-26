# Example 1: Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, File Handling!")

# Example 2: Reading a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Example 3: Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppending new content.")

# Example 4: Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Example 5: Handling file errors
try:
    with open("missing.txt", "r") as file:
        pass
except FileNotFoundError:
    print("File not found!")
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
