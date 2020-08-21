# Assertions

# we can make simple assetions with the assert keyword for testing purposes
# assert acceps an expression
# returns None if the expression is truthy
# raises an AssertionError if the expression is falsy
# accepts an optional error message as a second argument

def add_positive_numbers(x,y):
  assert x > 0 and y > 0, "Both numbers must be positive"
  return x + y

add_positive_numbers(1, 1)

# assert is not a function! it is a statement
# if a python file is run with -O flag (optimize mode) all assertions will not be evalulated -don't depend on them-