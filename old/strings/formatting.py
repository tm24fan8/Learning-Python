#!/usr/bin/env python3

# Basic formatting

name = 'Matt'
print('Hello {}'.format(name))

print('I:{} R:{} S:{}'.format(1, 2.5, 'foo'))

# Different possible formatting strings

print('Name: {}'.format('Paul'))
print('Name: {name}'.format(name='John'))
print('Name: {[name]}'.format({'name':'George'}))

# Formatting using integers for positions

print('Last {2} First: {0}'.format('Paul', 'George', 'John'))

# Additional formatting parameters

print("Name: {:*^12}".format("Ringo"))
print("Percent: {:=+10.1%}".format(-44/100))
print("Binary: {:b}".format(12))
print("Hex: {:x}".format(12))

# F-strings (Python 3.6)

print(f'My name is {name}')
print(f'My name is {name.capitalize()}')
print(f'Square root of two: {2**.5:5.3f}')
