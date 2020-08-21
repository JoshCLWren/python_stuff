# Abs
# return the absolute value of a number. The magnitude of a real number without regard to its sign. -5 would be 5

abs(-5) #5
abs(3.4444) #3.4444

# only works on ints and floats

# sum

# takes an iterable and an optional start
# returns the sum of start and the items of an iterable from left to right and returns the total

print(sum([1,2,3], 10))

# 10 is the OPTIONAL starting point

# round
#  return number rounded to ndigits precicions after the decimal


round(4.5) #5

def max_magnitude(lst):
  return max(abs(num) for num in lst)


def sum_even_values(*args):
  return sum(num for num in args if num % 2 == 0)



print(sum_even_values(1,2,3,4,5,6)) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0

def sum_floats(*args):
  return sum(num for num in args if type(num) == float)

print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
sum_floats(1,2,3,4,5) # 0