class Aquatic:
  def __init__(self, name):
    self.name = name
  def swim(self):
    return f"{self.name} is swimming"
  def greet(self):
    return f"I am {self.name} of the sea"

class Ambulatory:
  def __init__(self, name):
    self.name = name
  def walk(self):
    return f"{self.name} is walking"
  def greet(self):
    return f"I am {self.name} of the land!"

# only the first one on the left will run but you still have access to all the inherited methods
class Penguin(Ambulatory, Aquatic):
  def __init__(self, name):
    super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())

# Penguin inhertisn from aquatic and ambulaotry there instances of penguin can call both the walk and swim methods
# what about the greet methods? Why is it only calling the Aquatic.greet() instead of Ambulaotry.greet()

# Whenever a class is created Pytho sets a method resoultion order MRO for that class. Which is the order Python will look
# or methods on instances of that class.
# you can programmatically reference the MRO 3 ways:
# __mro__ attribute on the class
# use the mro() method on the class
# use the builtin help(cls) method

# print(Penguin.__mro__)
# print(Penguin.mro())
# print(help(Penguin))

class Mother:
  def __init__(self):
    self.eye_color = "brown"
    self.hair_color = "dark brown"
    self.hair_type = "curly"

class Father:
  def __init__(self):
    self.eye_color = "blue"
    self.hair_color = "blond"
    self.hair_type = "straight"

class Child(Mother, Father):
  pass
