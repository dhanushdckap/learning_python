# # Creating Variables in python
#
# x = 5
# y = "John"
# print(x) # answers is 5
# print(y) # answer is John
#
# # Casting
#
# x = str(3)
# y = int(3)
# z = float(3)
#
# print(x) # x will be '3'
# print(y) # y will be 3
# print(z) # z will be 3.0
#
# # Get the Type
#
# x = 5
# y = "John"
# print(type(x)) # x will be <class 'int'>
# print(type(y)) # y will be <class 'str'>
#
# # difference between Single or Double Quotes?
#
# x = "dhanush"
# # is the same as
# x = 'john'
#
# print(x)
#
# # Case-Sensitive
#
# a = 4
# A = "Sally"
# #A will not overwrite a
#
# print(a)
# print(A)
#
#
# ##-----------Variable Names----------##
#
# # Example
# # Legal variable names:
#
# myvar = "John"
# my_var = "John" # I select this method.
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John" # I select this method.
#
# # Multi Words Variable Names
#
# # Camel Case
# myVariableName = "John"
#
# # Pascal Case
# MyVariableName = "John" # I select this method.
#
# # Snake Case
# my_variable_name = "John" # I select this method.
#
# #-----------Assign Multiple Values----------##
#
# # Many Values to Multiple Variables
# x, y, z = "dhanush", "jeeva", "Gokulapriyan" # it taskes the values according to the order
# print(x) # dhanush
# print(y) # jeeva
# print(z) # Gokulapriyan

# # One Value to Multiple Variables
#
# x = y = z = "Orange"
# print(x) # x will be Orange
# print(y) # y will be Orange
# print(z) # z will be Orange

# # Unpack a Collection
#
# fruits = ["dhanush", "jeeva", "Gokulapriyan"]
# x, y, z = fruits
# print(x) # x will be dhanush
# print(y) # y will be jeeva
# print(z) # z will be Gokulapriyan

# #-----------Output Variables----------##

# x = "Dhanush is good boy"
# print(x) # this method is used for the see Output.
#
# # In the print() function, you output multiple variables, separated by a comma:
#
# x = "jeeva"
# y = "is"
# z = "also good boy"
# print(x, y, z)
#
# # You can also use the + operator to output multiple variables:
#
# x = "Gokulapriyan "
# y = "too "
# z = "good boy"
# print(x + y + z)
#
# # For numbers, the + character works as a mathematical operator:
#
# x = 5
# y = 10
# print(x + y) # answer will be 15
#
# # In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
#
# x = 5
# y = "John"
# print(x + y) # the error is
#
# # Traceback (most recent call last):
# #   File "Variables.py", line 118, in <module>
# #     print(x + y)
# # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# # The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
#
# x = 5
# y = "John"
# print(x, y) # answer : 5 John




