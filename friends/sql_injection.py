import sqlite3
conn = sqlite3.connect("users.db")
c = conn.cursor()
# query = "CREATE TABLE users (username TEXT, password TEXT)"
# c.execute(query)
# user_create = f"INSERT INTO users VALUES ('josh', '1234');"
# c.execute(user_create)
u = input("please enter your username...")
p = input("please enter your password...")
# query = f"SELECT * FROM users where username='{u}' AND password = '{p}'"# this allows people to add 'OR 1=1 ---

# c.execute(query)
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query, (u,p))# this won't allow somebody to add sql code since it's being passed as a tuple
result = c.fetchone()

if(result):
  print("welcome back")
else:
  print("failed login")

conn.commit()
conn.close()