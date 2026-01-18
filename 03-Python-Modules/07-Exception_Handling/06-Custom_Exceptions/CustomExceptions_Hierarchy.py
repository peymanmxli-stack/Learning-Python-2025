All exceptions inherit from:
BaseException
 ├── Exception
 │    ├── ValueError
 │    ├── TypeError
 │    ├── IndexError
 │    ├── KeyError
 │    ├── ZeroDivisionError
 │    ├── FileNotFoundError
 │    ├── PermissionError
 │    ├── ImportError
 │    ├── NameError
 │    ├── AttributeError
 │    └── RuntimeError
 ├── KeyboardInterrupt
 ├── SystemExit
 └── GeneratorExit
⚠️ Never catch BaseException
⚠️ Be careful with KeyboardInterrupt & SystemExit

Most Common Built-in Exceptions (You MUST know)
Exception	When it happens
ValueError	Wrong value
TypeError	Wrong type
IndexError	List index out of range
KeyError	Dict key not found
ZeroDivisionError	Divide by zero
FileNotFoundError	File doesn’t exist
PermissionError	No access rights
ImportError	Import failed
NameError	Variable not defined
AttributeError	Attribute missing
# ===========================================================================
# ===========================================================================

Exception Handling + Control Flow
Exception handling changes program flow:

Skips remaining code in try

Jumps to except

Executes finally

May crash or continue

That’s why it is part of Control Flow, not just errors.

# ===========================================================================
# ===========================================================================
  
Exception Handling vs Normal Flow
Situation	Use
Expected logic	if / else
Unexpected failure	try / except
Cleanup	finally
Rule enforcement	raise
# ===========================================================================
# ===========================================================================
  Final Count 
🔧 Exception Handling Components
Category	Count
Keywords	5
Structures	1 core pattern
Exception types	60+ built-in
Custom exceptions	Unlimited
# ===========================================================================
# 👤 Author
# ===========================================================================
👤 Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
