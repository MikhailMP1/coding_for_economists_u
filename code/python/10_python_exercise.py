# 1. Find headers/idxs for relevant vars: ISO_COUNTRY_CODE, WIN_COUNTRY_CODE
f = open('data/raw/european_commission/ted-sample.csv')

# Grab headers
headers = f.readline().strip().split(',')

# Make sure to close the file
f.close()

for index, value in enumerate(headers):
  print(index, value)

# WIN_COUNTRY_CODE at index 61

# 2. Instantiate an empty list called data
data = []

# 3. Use the context manager open() and
# 3.1  iterate through each row in ted-sample.csv and
# 3.2  append each row to the data list using (in the loop body)
#      data.append(list(line.split(",")))
with open('data/raw/european_commission/ted-sample.csv') as f:
  for line in f:
    data.append(list(line.split(",")))

print(data[0])
# Output should look like: data = [[row0], [row1], ..., [rowN]]
data = data[1:]  # Get rid of headers; don't need them.
# or data.pop(0)

# 4. Count the number of wins by country
d = {}
for row in data:
  country = row[61]  # Careful: some tenders are won by more than one country
  countries = country.split('---')  # Returns a list of winning countries
  for winning_country in countries:
    if not winning_country in d:
      d[winning_country] = 0
    d[winning_country] += 1

print(d)
