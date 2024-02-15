# First look at dictionaries

# A dictionary is a collection of key-value pairs.

# Synatx:
myDict = {"Dog": "Barks", "Cat": "Meows", "Whale": "Shreeks"}

print(myDict)

# We cannot use the same indexing syntax as with lists/str
# print(myDict[0]) # Produces an error

# Retrieve items of dictionary
print(myDict.items())

# We can use the key to get the value
print(myDict["Dog"])  # Barks

# We can also use the len() function
print(len(myDict))  # 3
