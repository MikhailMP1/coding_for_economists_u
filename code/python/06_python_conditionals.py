# Testing for equality
print(5 == 2)  # False

# Compare str to int (equality)
print('2' == 2)  # False

# Compare str to int (less than)
print('2' < 2)  # TypeError

# Testing for membership
print(2 in [1, 2, 3])  # True

# Testing for inequality
print(2 != 5)  # True

# Composite logical statements: and
print(2 == 2 and 5 == 5)  # Returns True only if both statements are True

# Composite logical statements: or
print(2 == 2 or 5 == 5)  # True
print(2 == 2 or 4 == 5)  # True

# Import libraries
import random

# Generate random numbers
random_number = random.randint(20, 34)

# Print message depending on value of random_number
if random_number < 25:
  print("The number is small.")
elif random_number < 30:
  print("The number is moderately high.")
else:
  print("It's a large number.")

# Nesting if statements
random_number1 = random.randint(1, 12)
random_number2 = random.randint(1, 16)

if random_number1 > 6:
  print("random_number1 is large.")

  if random_number2 > random_number1:
    print("random_number2 is larger than random_number1.")

# if statements with composite logical statements
random_number1 = random.randint(1, 12)
random_number2 = random.randint(1, 16)

if random_number1 > 6 or random_number2 > random_number1:
  print("random_number1 is large.")
  print("random_number2 is larger than random_number1.")
