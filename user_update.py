# import the csv functionality into pythong

# define a method called update_users that takes in an old first and last name and a new first and last name
# open the user.csv file and save it to as a list to a new variable to be read
# so we can iterate over it to find and update old names with new
# iniatialize a helper variable to ckeep track of how many users the funcion has updated
# reopen the file with the write only flag
# create another variable to write to the file
# iterate over the variale we iniatilized when we saved the variable to a list
# if we find an exact match for the old first and last name on the same row with the new values as an array
# if we don't match we'll need to write a row with the original value so that it gets left the way it was.
# write the new name to that row and update the count by 1
#
# return a string with users updated and the count.
#

import csv

def update_users(old_first, old_last, new_first, new_last):
  with open("users.csv") as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

  count = 0

  with open("users.csv", "w") as file:
    csv_writer = csv.writer(file)
    for row in rows:
      if row[0] == old_first and row[1] == old_last:
        csv_writer.writerow([new_first, new_last])
        count += 1
      else:
        csv_writer.writerow(row)

  return "Users updated: {}.".format(count)



print(update_users("Grace", "Hopper", "Hello", "World"))
print(update_users("Colt", "Steele", "Boba", "Fett"))
print(update_users("Not", "Here", "Still not", "Here"))