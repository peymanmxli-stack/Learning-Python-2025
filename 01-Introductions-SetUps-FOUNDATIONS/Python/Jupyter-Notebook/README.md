# 📓 Notebooks — Jupyter Usage Guidelines

This document defines **how Jupyter notebooks should be used, organized, and maintained** in this repository.

The goal is to keep notebooks **clean, educational, reproducible, and professional**.

---

## 📌 What Is This Folder For?

The `notebooks/` folder contains **Jupyter Notebook (`.ipynb`) files** used for:

* Learning Python step by step
* Experimenting with code
* Demonstrating concepts visually
* Data analysis and exploration

Notebooks here are **educational and experimental**, not production code.

---

## 🧠 Notebook Philosophy

Jupyter notebooks should:

* Explain **what** is happening
* Show **why** it matters
* Demonstrate **how** Python works

A good notebook reads like a **guided lesson**, not just code.

---

## 🗂️ Folder Structure

Recommended structure:

```
notebooks/
├── README.md
├── 01_introduction.ipynb
├── 02_variables.ipynb
├── 03_conditions.ipynb
├── 04_loops.ipynb
├── 05_functions.ipynb
└── 06_files.ipynb
```

---

## 🏷️ Naming Conventions

Follow these rules:

* Use **numbers** to keep order
* Use **snake_case**
* Use **clear and descriptive names**

Examples:

* `01_variables.ipynb` ✅
* `loops.ipynb` ❌
* `My Notebook.ipynb` ❌

---

## 🧩 Notebook Structure (Inside Each File)

Each notebook should contain:

1. **Title (Markdown cell)**
2. **Short explanation of the topic**
3. **Code cells** (small and focused)
4. **Markdown explanations between code**
5. **Outputs visible** (do not clear all results)

---

## 🔹 Code Cells — Best Practices

* Keep cells **short and readable**
* One concept per cell
* Avoid long scripts in a single cell
* Re-run notebooks from top to bottom before committing

---

## 🔹 Markdown Cells — Best Practices

Use Markdown cells to:

* Explain logic
* Describe results
* Add titles and sections

Example:

```markdown
## Example: Using a Loop
This cell demonstrates how a `for` loop works.
```

---

## 🧪 Kernel & Virtual Environment

Rules:

* Always use the project `.venv` as the kernel
* Do not use global Python
* If a notebook requires extra libraries, update `requirements.txt`

This guarantees reproducibility.

---

## 🚫 What NOT to Do

* ❌ Do not put production code in notebooks
* ❌ Do not mix unrelated topics
* ❌ Do not upload notebooks with broken cells
* ❌ Do not hardcode file paths specific to your computer

---

## 🔁 Notebooks vs Python Files

| Purpose        | Use         |
| -------------- | ----------- |
| Learning       | Notebook    |
| Experiments    | Notebook    |
| Documentation  | Notebook    |
| Libraries      | `.py` files |
| Final programs | `.py` files |

---

## 🏁 Final Notes

Used correctly, notebooks are a **powerful learning and teaching tool**.

Used incorrectly, they become confusing and unmaintainable.

Follow these rules to keep your notebooks **clean, useful, and professional**.

---

### ✍️ Author

**Peyman Miyandashti**
Polytechnic University of Baja California
Information Technology Engineering & Digital Innovation
From Mexico 🇲🇽
Year: 2025
ID: 250161
