# doctests
# we can write test for funciton sinide of the docstring
# write code that looks lite its inside of a REPL

def add(x,y):
  """add together x and y

  >>> add(1, 2)
  3
  >>> add(8, "hi")
  Traceback (most recent call last):
    ...
  TypeError: unsupported operand type(s) for +: 'int' and 'str'
  """

# def add(a,b):
#   """
#   >>> add(2,3)
#   5
#   >>> add(100, 200)
#   300
#   """
#   return a + b

def double(values):
  """ double the valueas in a list
  >>> double([1,2,3,4,5])
  [2,4,6,8,10]

  >>> double([])
  []

  >>> double(['a',b','c'])
  ['aa','bb','cc']

  >>> double([Ture, None])
  Traceback (most recent call last):
    ...
  TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
  """