# all
# return True if all elements of the iterable are truthy or if the iterable is empty

all([0,1,2,3]) #false
all([char for char in 'eio' if char in 'aeiou']) #true
all([num for num in [4,2,19,6,8] if num % 2 == 0]) #true

people = ["Charlie", "Casey", "Cody", "Carly", "Chrstina"]

all([name[0]=='C' for name in people])
# list comprehension are all people starting with C?

# any
# reutrn True if any element of the iterable is truthy

people.append("Tom")

any([name[0]=='T' for name in people]) # returns true

#list comprehension brackets are optional.

def is_all_strings(lst):
  return all([type(l) == str for l in lst])

# checks if lst is all strings type