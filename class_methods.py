# Class Methods
# not concerned with instances but the class itself
# include the @classmethod decorator

# class Person():
#   #...
#   @classmethod
#   def from_csv(cls, filename):
#     return cls(*params) #this is the same as callin Person(*params)

# Person.from_csv(my_csv)

# A User class with both instance attributes and instance methods
class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
  # cls refers to the class (User) similiar to how self is used but on the whole class
  # @ symbol is a decorator
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

  # the repr dunder method stands for representation of a class. This makes it so if your print(user) it will return this method
  def __repr__(self):
    return f"{self.first} is {self.age}"

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"



# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())












