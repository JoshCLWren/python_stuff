# # what's a decorator?
# # decorators are functions
# # decorators wrap other functions and enhace their behavior
# # decorators are examples of higher order functions
# # decorators have their own sytax using @ (sytactic sugar)

# # decorators as functions

# # def be_polite(fn):
# #   def wrapper():
# #     print("What a pleasure to meet you!!")
# #     # exececutes passed function
# #     fn()
# #     print("have a nice day")
# #   return wrapper
# # def greet():
# #   print("My name is Colt.")

# # greet = be_polite(greet)
# # greet()

# def rage():
#   print("I hate you")

# polite_rage = be_polite(rage)
# polite_rage()

# # decorator syntax
# # syntactic sugar

# def please_be_polite(fn):
#   def wrapper():
#     print("What a pleasure to meet you!")
#     fn()
#     print("have a nice day!")
#   return wrapper

# @please_be_polite # eliminates the need to assign the function to a variable and pass it the function
# def yeet():
#   print("My anem is Matt.")

# yeet()

# deocorators with different signatures
def shout(fn):
  def wrapper(*args, **kwargs):
    return fn(*args, **kwargs).upper()
  return wrapper

@shout
def greet(name):
  return f"Hi, I'm {name}."

@shout
def order(main, side):
  return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
  return "Lol"

print(order("burger", "fries"))
print(lol())