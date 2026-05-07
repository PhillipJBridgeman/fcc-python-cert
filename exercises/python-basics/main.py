"""
Filename: variables_and_naming.py
Description: Reference notes for Python variables, naming conventions,
             data types, and the print function.
Author: Phillip Bridgeman
Date: 2026-05-06
"""

# =============================================================================
# VARIABLES
# =============================================================================

# Variables are declared by assigning a value — no keyword needed (unlike JS or C#)
first_name = "Phillip"
age = 31

# Python is dynamically typed — the type is inferred from the assigned value
# You can reassign a variable to a different type (though this is rarely good practice)
x = 10      # int
x = "ten"   # now a str — Python allows this, but avoid it in real code


# =============================================================================
# NAMING CONVENTIONS
# =============================================================================

# Use snake_case for variable names (lowercase, words separated by underscores)
user_age = 31
favorite_color = "blue"

# Names must start with a letter or underscore — not a number
# valid_name = "ok"
# 1invalid = "error"  # SyntaxError

# Names are case-sensitive
name = "phillip"
Name = "PHILLIP"    # different variable from 'name'

# Avoid single-letter or vague names — they communicate no purpose
x = 56          # bad: what is x?
user_count = 56 # good: immediately clear

# Don't use Python reserved keywords as names
# if = 5        # SyntaxError — 'if' is reserved
# class = "Math"  # SyntaxError — 'class' is reserved

# =============================================================================
# COMMENTS
# =============================================================================

# Single-line comments start with a # symbol
# Python ignores everything after the # on that line

# Multi-line comments are just consecutive single-line comments
# Line one
# Line two
# Line three

# Use comments to explain WHY something is done, not WHAT the code does
# The code itself should be readable enough to show what it does

# =============================================================================
# DATA TYPES
# =============================================================================

# str — text, wrapped in single or double quotes
first_name = "Phillip"
city = 'Winnipeg'

# int — whole numbers
age = 31
year = 2026

# float — decimal numbers
height = 5.9
gpa = 3.58

# bool — True or False (capital first letter in Python)
is_student = True
is_tall = height > 6.0  # evaluated expression — False

# You can check the type of a variable with type()
print(type(first_name))  # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# isinstance() checks if a variable matches a specific type — returns True or False
print(isinstance(age, int))           # True
print(isinstance(first_name, str))    # True
print(isinstance(height, float))      # True
print(isinstance(is_student, bool))   # True
print(isinstance(age, str))           # False — age is int, not str

# =============================================================================
# PRINT FUNCTION
# =============================================================================

# print() outputs data to the terminal
print("Hello world!")

# Multiple arguments are separated by commas — Python adds a space between them
print("My name is", first_name, "and I am", age, "years old.")
# Output: My name is Phillip and I am 31 years old.

# print() moves to a new line after each call by default
print("Line one")
print("Line two")

# Use end= to change what print adds at the end (default is newline \n)
print("Same ", end="")
print("line")  # Output: Same line

# Use sep= to change the separator between arguments (default is a space)
print("Winnipeg", "Manitoba", "Canada", sep=", ")
# Output: Winnipeg, Manitoba, Canada

# =============================================================================
# STRINGS
# =============================================================================

# Strings are sequences of character(s) enclosed in quotes

# Example of strings
greeting = "Hello"
name = 'Alice'
letter = "A"

# String can be used with various operations
# Concatenation (joining strings)
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!

# Repetition
echo = "Echo! " * 3
print(echo)  # Output: Echo! Echo! Echo!

# String indexing (accessing individual characters)
first_letter = name[0]  # 'A' (indexing starts at 0)
last_letter = name[-1]  # 'e' (negative indexing starts from the end)

# Slicing (extracting a substring)
sub_name = name[1:4]  # 'lic' (from index 1 to 3)
sub_greeting = greeting[:3]  # 'Hel' (from start to index 2)

# String methods (built-in functions for strings)
upper_greeting = greeting.upper()  # 'HELLO'
lower_name = name.lower()          # 'alice'
title_name = name.title()          # 'Alice'

# f-strings (formatted string literals) for embedding expressions
age_next_year = age + 1
print(f"Next year, I will be {age_next_year} years old.")
# Output: Next year, I will be 32 years old.

# String formatting with format() method
formatted_greeting = "Hello, {}. You are {} years old.".format(name, age)
print(formatted_greeting)  # Output: Hello, Alice. You are 31 years old.

# String formatting with % operator (older style)
percent_greeting = "Hello, %s. You are %d years old." % (name, age)
print(percent_greeting)  # Output: Hello, Alice. You are 31 years old.

# Triple quotes for multi-line strings
multi_line = """This is a
multi-line string."""
print(multi_line)
# Output:
# This is a
# multi-line string.

# Escape characters for special characters in strings
quote = "She said, \"Hello!\""  # Use backslash to escape double quotes
print(quote)  # Output: She said, "Hello!"

# Raw strings to ignore escape characters (useful for file paths)
raw_path = r"C:\Users\Phillip\Documents"
print(raw_path)  # Output: C:\Users\Phillip\Documents

# String concatenation with variables
first_name = "Phillip"
last_name = "Bridgeman"
full_name = first_name + " " + last_name
print(full_name)  # Output: Phillip Bridgeman

# String interpolation with f-strings
age = 31
print(f"My name is {full_name} and I am {age} years old.")
# Output: My name is Phillip Bridgeman and I am 31 years old.
