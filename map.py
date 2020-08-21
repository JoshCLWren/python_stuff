num = [2, 4, 6, 8, 10]

doubles = list(map(lambda x: x*2, num))

print(doubles)

people = ["josh", "me", "too"]

peeps = map(lambda name: name.upper(), people)

list(peeps)

print(peeps)

# map(function or lambad here: iterator, what you are iteratin) returns the item mapped with the function performed on each element in it

nums = [1,2,3,4]

def decrement_list(nums):
  return list(map(lambda numbers: numbers - 1, nums))

print(decrement_list(nums))