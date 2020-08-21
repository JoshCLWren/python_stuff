# Iterator
# any object that can be iterated on
# next() can be called on
# iterable: an object that returns and iterator

name = "Oprah"
# next(name) # won't work due to not being an iternator
it = iter(name)
# next() is called on an iterator the iternator returns the next item until it raises a StopIteration error
next(it) # O

# custom for loop

def my_for(iterable, func):
  iterator = iter(iterable)
  while True:
    try:
      thing = (next(iterator))
    except StopIteration:
      print("End of iterator")
      break
    else:
      func(thing)

my_for("hello", print)
my_for([1,2,3,4], print)

class Counter:
  def __init__(self, low, high):
    self.current = low
    self.high = high
  def __iter__(self):
    return self
  def __next__(self):
    if self.current < self.high:
      num = self.current
      self.current += 1
      return num
    raise StopIteration


for n in Counter(50,55):
  print(n)

# Generators are iterators
# functions vs. genererator functions
#  functions | Generators
# uses return | uses yield
# returns once | can yield multiple times
# when invoked returns the return value | when invoked returns a generator

def count_up_to(max):
  count = 1
  while count <= max:
    yield count
    count += 1
# keeps track of state until next is called

counter = count_up_to(5) # returns a generator object

next(counter) #1
next(counter) #2
next(counter) #3
next(counter) #4
next(counter) #5

def yes_or_no():
  answer = "yes"
  while True:
    yield answer
    answer = "no" if answer == "yes" else "yes"

gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'

#infiinte generators
# def current_beat():
#   max = 100
#   nums = (1,2,3,4)
#   i = 0
#   result = []
#   while len(result) < max:
#     if i >= len(nums): i = 0
#     result.append(nums[i])
#     i += 1
#   return result
# print(current_beat())

def current_beat():
  nums = (1,2,3,4)
  i = 0
  while True:
    if i >= len(nums): i = 0
    yield nums[i]
    i += 1
# generates a "beat" every time next is called on and resets back to 1 after 4 indefinelty

# def make_song(verses=99, beverage="soda"):
#   # first arg in range takes in start, second stop, 3rd step
#   for num in range(verses, -1, -1):
#     if num > 1:
#       yield print(f"{num} bottles of {beverage} on the wall.")
#     elif num == 1:
#       yield print(f"Only {num} botle of {beverage} left!")
#     else:
#       yield print(f"no more {beverage}!")
#       break



# kombucha_song = make_song(5, "kombucha")
# next(kombucha_song)
# next(kombucha_song)
# next(kombucha_song)
# next(kombucha_song)
# next(kombucha_song)
# next(kombucha_song)
# next(kombucha_song)

def get_multiples(number=2, count=10):
  next_num = number
  while count > 0:
    yield next_num
    count -= 1
    next_num += number

default_multiples = get_multiples()
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))
print(next(default_multiples))


def get_unlimited_multiples(number=1):
  next_num = number
  while True:
    yield next_num
    next_num += number

sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])