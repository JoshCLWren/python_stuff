import csv

def delete_users(first, last):

  with open("users.csv") as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

  count = 0

  with open("users.csv", "w") as file:
    csv_writer = csv.writer(file)
    for row in rows:
      if row[0] == first and row[1] == last:
        count += 1
      else:
        csv_writer.writerow(row)

  return "Users deleted: {}.".format(count)


print(delete_users("Grace", "Hopper"))
print(delete_users("Colt", "Steele"))
print(delete_users("Not", "Here"))