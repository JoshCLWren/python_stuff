def reverse_string(string):
  return string [::-1]

print(reverse_string("test"))

# check if the values in a list are lists
def list_check(lst):
  for x in lst:
    if type(lst) == list():
      return True
  return False

list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True

# accepts a list and returns a new list with every second value removed
def remove_every_other():
  pass

remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 