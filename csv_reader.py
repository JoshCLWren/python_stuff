# csv
# comma seperted values
# common format for tabular data
# csv moudle
# reader lets you iterate over rows of the csv as lists
# dictreader = lets yo iterate over rowas of the csv as ordered Dicts

from csv import reader
with open("fighters.csv") as file:
  csv_reader = reader(file)
    # each row is a list
  next(csv_reader)
  for fighter in csv_reader:
      print(f"{fighter[0]} is from {fighter[1]}")

from csv import DictReader
with open("fighters.csv") as file:
    # ordered dictionaries automatically use the headers as the keys
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row['Name'])