# what is oop?
# using classes or objects to model some process or thing in the world
# class = blueprint for objects that can contain methods and attributes
# instance = objects that are constructed from a class blueprint that contain their class's methods and props
# why oop?
# _ before class for "private"
# Encapsulation
# the grouping of public and private attribs and methods into a programmattic class, making abstraction possible
# Absstraction
# exposing only "relevant" data in a class interface, hiding private attribs and methods

# defining the simplest possible class. convention is camel case for classes

class User:
  pass

# instantiate the class this way
user1 = User()

print(user1)

class Vehicle:
  pass

car = Vehicle()
boat = Vehicle()