# Polymorphism
# an object can take on many from
# 1 the same class method works in a similiar way for different classes
# using method overriding by having a method in base or parent class that is overridden by a subclass
# each subclass will have a different implementation of the method

class Animal:
  def speak(self):
    raise NotImplementedError("Sublcass needs to implement this method")
class Dog(Animal):
  def speak(self):
    return "woof"
class Cat(Animal):
  def speak(self):
    return "meow"
class Fish(Animal):
  pass

# 2 the same operation works for different kinds of objects

8 + 2 # 10 integers
"8" + "2" #82 strings


