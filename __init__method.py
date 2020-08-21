# __init__ method

# anytime you make a class python the special __init__ method will get called every time you create instantiate said class

class User:
  # pass self first!
  def __init__(self, first, last, age):
    print("User class instantiated")
    self.first = first
    self.last = last
    self.age = age


user1 = User("Joe", "Smith", 68)

print(user1.first)

# self keyword referrs to the specific instance of the class we are working with

class Comment:
  # likes are defaulted to 0
  def __init__(self, username, text, likes=0):
    self.username = username
    self.text = text
    self.likes = likes

c = Comment("dude", "lol", 3)

class Person:
  # dunder methods have double uderscored methods like __init__
  def __init__(self):
    self.name = "Tony"
    # convention for private doesn't do anything but signal to other devs that its private. Python doesn't have private
    self._secret = "hi!"
    # name mangling - makes this particular to this class and unique. Python will add the class name to = _Person__msg
    self.__msg = "I like turtles"

p = Person()

print(p.name)
print(p._secret)
# how to access a name mangle
print(p._Person__msg)