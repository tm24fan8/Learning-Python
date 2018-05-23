#!/usr/bin/env python3

# Print name and age with formatting
name = "Tony"
age = 29

print(f'My name is {name}, and I am {age} years old.')

# Create paragraph variable with formatting

paragraph = f""""Python is a great language!", said {name}. "I don't ever remember having this much fun before.\""""
print(paragraph)

# Unicode formatting of Omega in both code point and Unicode name

print("\u03A9")
print("\N{GREEK CAPITAL LETTER OMEGA}")

# Variables showing car cost

item = "car"
cost = 13499.99

print(f'{item:<10}{cost:>10}')
