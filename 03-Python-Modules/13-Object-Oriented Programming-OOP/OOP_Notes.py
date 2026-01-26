"""
====================================================
OBJECT-ORIENTED PROGRAMMING (OOP)
DEEP THEORY & PROFESSIONAL NOTES
====================================================

This file provides a complete and professional explanation
of Object-Oriented Programming (OOP) in Python.

OOP is a programming paradigm that structures software
around objects and classes instead of functions and logic alone.
"""

# ====================================================
# 1. WHAT IS A CLASS?
# ====================================================
"""
A class is a blueprint or template used to create objects.

It defines:
• What data an object will have (attributes)
• What actions an object can perform (methods)

A class does NOT represent a real object.
It represents the idea or structure of an object.

Think of a class as:
📐 A blueprint
🏗 A design
📄 A specification
"""

class Person:
    pass


# ====================================================
# 2. WHAT IS AN OBJECT?
# ====================================================
"""
An object is an instance of a class.

It is a real, usable entity created from a class.

If a class is a blueprint,
an object is the actual product built from it.

✔ Objects store real data
✔ Objects can call methods
✔ Multiple objects can come from one class
"""

person1 = Person()
person2 = Person()


# ====================================================
# 3. THE __init__ METHOD (CONSTRUCTOR)
# ====================================================
"""
The __init__ method is a special method called a constructor.

It runs automatically when a new object is created.

Its purpose is to:
✔ Initialize object data
✔ Assign initial values to attributes
"""

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


# ====================================================
# 4. ATTRIBUTES
# ====================================================
"""
Attributes are variables that belong to an object.

They represent the state or data of an object.

Types of attributes:
1️⃣ Instance attributes (most common)
2️⃣ Class attributes (shared across objects)
"""

class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand, year):
        self.brand = brand      # Instance attribute
        self.year = year


# ====================================================
# 5. METHODS
# ====================================================
"""
Methods are functions defined inside a class.

They describe behaviors or actions of an object.

Methods:
✔ Operate on object data
✔ Use self to access attributes
✔ Define object functionality
"""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


# ====================================================
# 6. THE `self` KEYWORD
# ====================================================
"""
`self` represents the current object instance.

It allows:
✔ Accessing attributes
✔ Calling other methods
✔ Differentiating object data

Without `self`, Python cannot know
which object's data is being used.
"""

class Device:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)


# ====================================================
# 7. ENCAPSULATION
# ====================================================
"""
Encapsulation means restricting direct access
to an object's internal data.

It protects data from accidental modification.

Python uses naming conventions:
✔ Public       → attribute
✔ Protected    → _attribute
✔ Private      → __attribute
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance


# ====================================================
# 8. INHERITANCE
# ====================================================
"""
Inheritance allows one class to inherit
attributes and methods from another class.

Benefits:
✔ Code reuse
✔ Logical hierarchy
✔ Extensibility
"""

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")


# ====================================================
# 9. POLYMORPHISM
# ====================================================
"""
Polymorphism means:
"Same method name, different behavior"

It allows different objects
to respond differently to the same method call.
"""

class Cat:
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()


# ====================================================
# 10. ABSTRACTION
# ====================================================
"""
Abstraction hides complex implementation
and shows only essential functionality.

It focuses on:
✔ What an object does
✔ Not how it does it

Python uses the abc module for abstraction.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# ====================================================
# 11. OOP BEST PRACTICES
# ====================================================
"""
✔ Use meaningful class names (PascalCase)
✔ One class = one responsibility
✔ Keep methods small and focused
✔ Protect sensitive data (encapsulation)
✔ Favor composition when possible
✔ Avoid deep inheritance chains
✔ Write readable and maintainable code
✔ Think in objects, not scripts
"""

# ====================================================
# END OF NOTES — OOP
# ====================================================

"""
👤 Author
Peyman Miyandashti
🎓 Polytechnic University of Baja California
💻 Information Technology Engineering & Digital Innovation
📍 From Mexico
📅 Year: 2026
🆔 ID: 250161
"""
