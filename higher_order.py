# functions can be passes as args to other functions...

def sum(n, func):
  total = 0
  for num in range(1, n+1):
   total += func(num)
  return total
def square(x):
  return x*x
def cube(x):
  return x*x*x

print(sum(3,square))
print(sum(3,cube))

# functions can be nested inside other functions
from random import choice

def greet(person):
  def get_mood():
    msg = choice(("Hello there ", "Go away ", "I love you "))
    return msg
  result = get_mood() + person
  return result

print(greet("Toby"))

#  we can return funcs from other funcs

def make_laugh_func():
  def get_laugh():
    l = choice(('hahahaha', 'lol', 'teheheh'))
    return l
    # this returns a function!
  return get_laugh

laugh = make_laugh_func()
print(laugh())

# inner functions can access outer function scope

def make_laugh_at_func(person):
  def get_laugh():
    laugh = choice(("hahahahah", "lol", "tehehehe"))
    # person is not passed in or passed into get_laugh but it's in scope (closure)
    return f"{laugh} {person}"
  return get_laugh

laugh_at = make_laugh_at_func("Linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())