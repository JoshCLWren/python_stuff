from time import time
from functools import wraps

# def speed_test(fn):
#   def wrapper(*args, **kwargs):
#     start_time = time()
#     result = fn(*args, **kwargs)
#     end_time = time()
#     print(f"Executing {fn.__name__}")
#     print(f"Time Elapsed: {end_time - start_time}")
#     return result
#   return wrapper

# @speed_test
# def sum_nums_gen():
#   return sum(x for x in range(500000))

# @speed_test
# def sum_nums_list():
#   return sum([x for x in range(500000)])

# print(sum_nums_gen())
# print(sum_nums_list())
# #  we can return funcs from other funcs

# # def make_laugh_func():
# #   def get_laugh():
# #     l = choice(('hahahaha', 'lol', 'teheheh'))
# #     return l
# #     # this returns a function!
# #   return get_laugh

# # laugh = make_laugh_func()
# # print(laugh())
# # from functools import wraps

# # def show_args(fn):
# #     @wraps(fn)
# #     def wrapper(*args, **kwargs):
# #         print("Here are the args:", args)
# #         print("Here are the kwargs:", kwargs)
# #         return fn(*args, **kwargs)
# #     return wrapper

# def ensure_no_kwargs(fn):
#   @wraps(fn)
#   def wrapper(*args, **kwargs):
#     if kwargs:
#       raise ValueError("No Kwargs allowed...")
#     return fn(*args, **kwargs)
#   return wrapper

# @ensure_no_kwargs
# def greet(name):
#   print(f"Hi there {name}")

# # greet(name="Tony")

# def double_return(fn):
#   @wraps(fn)
#   def wrapper(*args, **kwargs):
#     val = fn(*args, **kwargs)
#     return [val, val]
#   return wrapper

# @double_return
# def add(x, y):
#     return x + y

# add(1, 2) # [3, 3]

# @double_return
# def greets(name):
#     return "Hi, I'm " + name

# print(greets("dgsfhgjhkj"))

# def ensure_fewer_than_three_args(fn):
#   @wraps(fn)
#   def wrapper(*args, **kwargs):
#     if len(args) < 3:
#       return fn(*args, **kwargs)
#     return "Too Many arguments"
#   return wrapper

# @ensure_fewer_than_three_args
# def add_all(*nums):
#     return sum(nums)

# print(add_all()) # 0
# print(add_all(1)) # 1
# print(add_all(1,2)) # 3
# print(add_all(1,2,3)) # "Too many arguments!"
# print(add_all(1,2,3,4,5,6)) # "Too many arguments!"

# def only_ints(fn):
#   @wraps(fn)
#   def wrapper(*args, **kwargs):
#     if any([arg for arg in args if type(arg) != int]):
#       return "Please only invoke with integers"
#     return fn(*args, **kwargs)
#   return wrapper

# @only_ints
# def add(x, y):
#     return x + y

# print(add(1, 2)) # 3
# print(add("1", "2")) # "Please only invoke with integers."

# def ensure_authorized(fn):
#   @wraps(fn)
#   def wrapper(*args, **kwargs):
#     if kwargs.get("role") == "admin":
#       return fn(*args, **kwargs)
#     return "Unauthorized"
#   return wrapper

# @ensure_authorized
# def show_secrets(*args, **kwargs):
#     return "Shh! Don't tell anybody!"

# print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
# show_secrets(role="nobody") # "Unauthorized"
# show_secrets(a="b") # "Unauthorized"

# decorators that take an argument

# def ensure_first_arg_is(val):
#   # first layer passes the arg
#   def inner(fn):
#     # second layer takes the function
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#       # thrid layer does the work
#       if args and args[0] != val:
#         return f"first arg needs to be {val}"
#       return fn(*args, **kwargs)
#     return wrapper
#   return inner

# @ensure_first_arg_is("burrito")
# def fav_foods(*foods):
#   print(foods)

# print(fav_foods("burriot", "ice cream"))

# @ensure_first_arg_is(10)
# def add_to_ten(num1, num2):
#   return num1 + num2

# print(add_to_ten(10,12))
from time import sleep

def delay(timer):
  def inner(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      print("Waiting {}s before running {}".format(timer, fn.__name__))
      sleep(timer)
      return fn(*args, **kwargs)
    return wrapper
  return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"



