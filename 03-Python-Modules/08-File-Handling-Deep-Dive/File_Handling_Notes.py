"""
FILE HANDLING — THEORY & NOTES

Python provides built-in functions to work with files.

Basic syntax:
file = open("filename", "mode")
file.close()

Recommended syntax (safe):
with open("filename", "mode") as file:
    operations

Common file modes:
r  -> Read
w  -> Write (overwrite)
a  -> Append
rb -> Read binary
wb -> Write binary

Important:
- Opening a non-existing file in 'r' raises FileNotFoundError
- 'w' creates the file if it does not exist
- 'with' ensures automatic file closure
"""

# Example
with open("notes.txt", "w") as f:
    f.write("File handling basics")
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
