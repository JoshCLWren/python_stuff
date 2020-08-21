# class Pet:
#   allowed = ['cat', 'dot', 'fish', 'rat']
#   def __init__(self, name, species):
#     if species not in Pet.allowed:
#       raise ValueError(f"You can't have a {species} as a pet!")
#     self.name = name
#     self.species = species
#   def set_species(self, species):
#     if species not in Pet.allowed:
#       raise ValueError(f"You can't have a {species} as a pet!")
#     self.species = species



# cat = Pet("Blue", "cat")
# dog = Pet("Wyatt", "Tiger")

class Chicken:
  total_eggs = 0
  def __init__(self, species, name, eggs=0):
    self.species = species
    self.name = name
    self.eggs = eggs
  def lay_egg(self):
    Chicken.total_eggs += 1
    self.eggs += 1
    return self.eggs

c1 = Chicken(name="Alice", species="PAt")
print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)

