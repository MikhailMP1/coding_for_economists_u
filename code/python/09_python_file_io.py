# Read text files

# Open
file = open('data/raw/european_commission/ted-sample.csv')

print(file.readline())
print(file.readline())

file.close()

# Here we have to close the file manually; not ideal

# Context manager
with open('data/raw/european_commission/ted-sample.csv') as file:
  for line in file:
    print(line)