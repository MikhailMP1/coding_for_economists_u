# Intro to data type set

# set is a collection of well defined objects
mySet = {1, 2, 3}
print(mySet)

# Check type
print(type(mySet))

# Sets only contain unique values
mySet = {1, 2, 3, 3}  # Duplicate 3 gets removed
print(mySet)

# Check membership
print(1 in mySet)

print(set('aaaaaaabbbbbbbbbbbbcccccccc'))

# Define two sets and check out set operations
setA = {1, 2, 3}
listB = [3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
setB = set(listB)

print(setA, setB)

# Set union
unionAB = setA | setB
print(unionAB)

# Intersection
intersecAB = setA & setB
print(intersecAB)
