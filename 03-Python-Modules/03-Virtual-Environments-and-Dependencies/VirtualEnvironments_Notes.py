"""
📦 Module — Virtual Environments & Dependencies
📘 Professional Notes

Virtual environments allow Python projects to run in isolated spaces.
Each project can have its own dependencies and versions without affecting
other projects or the system Python installation.

This file explains the concepts, commands, and best practices used in
professional Python development.
"""


# ===========================================================================
# 🧠 1. What Is a Virtual Environment?
# ===========================================================================
# A virtual environment is an isolated Python environment that contains:
# - its own Python interpreter
# - its own site-packages directory
# - its own installed libraries
#
# This isolation prevents conflicts between projects.


# ===========================================================================
# ❓ 2. Why Virtual Environments Are Necessary
# ===========================================================================
# Without virtual environments:
# - Libraries are installed globally
# - Different projects may require different versions
# - Upgrading a package can break existing projects
#
# With virtual environments:
# - Each project controls its dependencies
# - Reproducibility is improved
# - Collaboration becomes safer and easier


# ===========================================================================
# 🐍 3. System Python vs Virtual Environment Python
# ===========================================================================
# System Python:
# - Installed by the OS
# - Used by system tools
# - Should NOT be modified heavily
#
# Virtual Environment Python:
# - Created per project
# - Safe to install and remove packages
# - Can be deleted without affecting the system


# ===========================================================================
# 🛠️ 4. Creating a Virtual Environment
# ===========================================================================
# Python includes the built-in venv module.
#
# Command (run in terminal):
#   python -m venv venv
#
# "venv" is the folder name (commonly used).
# You can name it differently if needed.


# ===========================================================================
# ▶️ 5. Activating a Virtual Environment
# ===========================================================================
# Activation depends on the operating system.

# Windows (PowerShell / CMD):
#   venv\Scripts\activate

# macOS / Linux:
#   source venv/bin/activate

# After activation:
# - The terminal shows the environment name
# - "python" and "pip" refer to the virtual environment


# ===========================================================================
# ⏹️ 6. Deactivating a Virtual Environment
# ===========================================================================
# To exit the virtual environment:
#
#   deactivate
#
# This returns you to the system Python.


# ===========================================================================
# 📦 7. Installing Packages with pip
# ===========================================================================
# pip installs packages into the active environment only.
#
# Examples:
#   pip install requests
#   pip install numpy
#   pip install django
#
# Always activate the environment before installing packages.


# ===========================================================================
# 🔍 8. Viewing Installed Packages
# ===========================================================================
# To list installed packages:
#
#   pip list
#
# To see package details:
#
#   pip show requests


# ===========================================================================
# 🧾 9. requirements.txt (Dependency Snapshot)
# ===========================================================================
# A requirements.txt file stores exact dependency versions.
#
# To create it:
#   pip freeze > requirements.txt
#
# To install dependencies from it:
#   pip install -r requirements.txt
#
# This ensures reproducible environments.


# ===========================================================================
# 🔁 10. Recreating a Virtual Environment
# ===========================================================================
# Common workflow:
# 1. Delete old venv folder
# 2. Create a new virtual environment
# 3. Activate it
# 4. Install dependencies from requirements.txt
#
# This guarantees a clean setup.


# ===========================================================================
# ⚠️ 11. Common Mistakes
# ===========================================================================
# ❌ Installing packages without activating the environment
# ❌ Committing the venv folder to GitHub
# ❌ Forgetting to update requirements.txt
# ❌ Mixing global and local dependencies


# ===========================================================================
# ✅ 12. Best Practices
# ===========================================================================
# ✔ Always create a virtual environment per project
# ✔ Name it "venv" for consistency
# ✔ Add venv/ to .gitignore
# ✔ Use requirements.txt
# ✔ Activate environment before coding or installing packages
# ✔ Keep dependencies minimal


# ===========================================================================
# 🧠 13. Summary
# ===========================================================================
# In this module, I learned:
# - What virtual environments are
# - Why dependency isolation matters
# - How to create and activate virtual environments
# - How to manage dependencies with pip
# - How to use requirements.txt
# - Best practices used in professional projects


# ===========================================================================
# 👤 Author
# ===========================================================================
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161

# 🏁 End of Notes
# ===========================================================================
