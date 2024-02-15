# # Basic arithmetic operations in Python

# # Add two numbers
# print(2 + 4)

# # Divide two numbers
# print(10 / 5)

# # Careful: division returns a float
# print(type(10 / 5))

# # Exponentiation
# print(2**3)

# # Assigning variables
# x = 5
# y = x**2
# print(y)

# String
a = "Hello how're you?"

# Arithmetic operations on strings
# Multiplication
print(a * 5)

# Concatenation
b = "I'm good, thank you."
print(a + " " + b)

# Substraction
# print(a - b)

# Division
# print(a / b)

# Indexing and slicing
# First element
print(a[0])

# Last element
print(a[-1])

# Slicing
print(a[0:5])

# How many characters does our string have?
print(f'Our string a has {len(a)} characters')

# Alternatively
print('Our string a has {} characters'.format(len(a)))

# Have a look at logical statements
print(2 == 2)  # True (equivalent to 1)

print(2 == 3)  # False (equivalent to 0)

# Check if True and 1 are in fact equivalent
print(True == 1)

# True evaluates to 1 and False evaluates to zero
print(True + True + True)

# Check equivalence of two variables
print(a == b)

# Multiple logical statements
print(2 == 2 and 3 == 3)  # True
print(2 == 2 and 3 == 4)  # False

print(2 == 2 or 3 == 4)  # True
print(2 == 3 or 3 == 4)  # False

# Testing for inequality
print(2 != 3)  # True

# Testing for less than/more than
print(2 < 3)  # True
print(2 > 3)  # False
