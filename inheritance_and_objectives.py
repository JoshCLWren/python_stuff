# objectives
# implement inheritance including multiple
# method resolution order
# polymorphisms
# special methods

# inheritance
# the abilty to define a class whcich inherits from another class a base or parent class
# inheritance works by passing the parent class as an arg to the definiation of a childe classs

class Animal:
  cool = True
  def make_sound(self, sound):
    print(f"this animal says {sound}")


class Cat(Animal):
  pass

gandalf = Cat()
gandalf.make_sound("meow")
gandalf.cool