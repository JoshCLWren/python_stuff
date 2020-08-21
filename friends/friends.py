# creating a sql table with Python.
# and manipulating tables
import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# INSERTING WITH PTYHON
# insert_query = "INSERT INTO friends VALUES ('Merriwehter', 'Lewis', 7);"
# don't do this
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
# better way
# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# # the ? allows us to pass a tuple with the value
# c.execute(query, (form_first,))
# data = ("Steve", "Irwin", 9)
# query = f"INSERT INTO friends VALUES (?,?,?)"
# c.execute(query, data)
# commit changes

# BULK INSERTS WITH PYTHON
#
people = [
	("Roald","Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil","Armstrong", 7),
	("Daniel", "Boone", 3)]
# executemany works but a for loop will let you do other math and calculations alongs side it
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
# average = 0
# for person in people:
#   c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#   average += person[2]
# print(average/len(people))

# SELECTING WITH PYTHON

c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

# # for result in c:
# #   print(result)
# # fetchall does the same in less lines
# print(c.fetchall())#fetchall returns a list
# # print(c.fetchone())#returns the first match

# SQL INJECTION!!!



conn.commit()
conn.close()