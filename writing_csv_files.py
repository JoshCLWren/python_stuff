# writing csv files
# writer - creates a writer object for writng to csv
# writerow

# from csv import writer
# with open("fighters2.csv", "w") as file:
#   csv_writer = writer(file)
#   csv_writer.writerow(["Character", "Move"])
#   csv_writer.writerow(["Ryu", "Hadouken"])

from csv import reader, writer
with open('fighters.csv') as file:
  csv_reader = reader(file)
  fighters = [[s.upper() for s in row] for row in csv_reader]
  for row in csv_reader:
    print(row)

with open('screamin_fighters.csv', 'w') as file:
  csv_writer = writer(file)
  for fighter in fighters:
    csv_writer.writerow(fighter)

# using dictionaire
# DictWriter - creates a writer object for writing using dictionaries
# fieldnames - kwarg for the dictwriter specifiying headers
# writeheader -mehtod on a writer to write header row
# writerow - method on a writer to write a row based on a dict

from csv import writer, DictWriter, DictReader

with open("cats.csv", "w") as file:
  headers = ["Name", "Breed", "Age"]
  csv_writer = DictWriter(file, fieldnames=headers)
  csv_writer.writeheader()
  csv_writer.writerow({
    "Name": "Garfield",
    "Breed": "Orange Tabby",
    "Age": 10
  })

def cm_to_in(cm):
  return float(cm) * 0.393701

with open("fighters.csv") as file:
  csv_reader = DictReader(file)
  fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
  headers = ("Name", "Country", "Height")
  csv_writer = DictWriter(file, fieldnames=headers)
  csv_writer.writeheader()
  for f in fighters:
    csv_writer.writerow({
      "Name": f["Name"],
      "Country": f["Country"],
      "Height": cm_to_in(f["Height (in cm)"])
    })



# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson


def add_user(first, last):
  # the a flag adds to the file and doesn't overwrite
  with open("users.csv", "a") as file:
    csv_writer = writer(file)
    csv_writer.writerow([first, last])

add_user("Dwayne", "Johnson") # None

def print_users():
  with open("users.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
      print("{} {}".format(row['First Name'], row['Last Name']))

print_users()

def find_user(first, last):
