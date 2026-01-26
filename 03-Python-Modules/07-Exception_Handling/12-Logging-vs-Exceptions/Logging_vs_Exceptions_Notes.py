"""
LOGGING VS EXCEPTIONS — THEORY & NOTES

Exceptions:
- Used to signal errors
- Control program flow
- Stop execution when something is wrong

Logging:
- Used to record information
- Does NOT stop execution
- Helps debugging and monitoring

Logging levels:
DEBUG    → Detailed internal information
INFO     → Normal application flow
WARNING  → Something unexpected but recoverable
ERROR    → Serious problem
CRITICAL → Program may not continue

Rule of thumb:
- Raise exceptions for incorrect states
- Log events for visibility
"""

import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
