# write a function which accepts a string and returns a new string with all the cars reversd
print("***********remove_ever_other")
def reverse_string(string):
  return string [::-1]

print(reverse_string("123456789"))

# slice notation:
# a[start:stop:step]
# [-1] last item in array
# [-2:] last two items in the array
# [:-2] everthing except the last two items
# [::-1] all times reversed
# [1::-1] the first two items reversed
# [:-3:-1] the last two items reversed
# [-3::-1] everthing ecept the last two items reversed
# a[start:stop:step] == a[slice(start, stop, step)]

# write a funciton called list_check which accepts a list and returns True if each value in the list is a list. Otherwise false
print("**************list_check")
def list_check(lst):
  for i in lst:
    if isinstance(i, list) == False:
      return False
  return True

print(list_check([[1,2],[2,3], 1]))

print("***********remove_every_other")

# write a funciton called remove_every_other that accepts a list and returns a new list with every second value removed.

def remove_every_other(lst):
  return lst [::2]

print(remove_every_other([1,2,3,4,5])) # [1,3,5]
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1])) # [1]

print("***************sum_pairs)")

# write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed to the function

def sum_pairs(lst, magic_number):
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
      if lst[i] + lst[j] == magic_number:
        return [lst[i],lst[j]]
      else:
        return []


print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
print(sum_pairs([11,20,4,2,1,5], 100)) # []

# write a functino called vowell count that accepts a string and return a dict with the keys as the vowells and the values as the count of times that vowel appers in the string
print("************vowel_count")

def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}



print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1})
print(vowel_count('Elie')) # {'e': 2, 'i': 1)}
print(vowel_count('Colt')) # {'o': 1}

print("**********titleize")

# write a function called titleze which accepts a string of words and returns a new string with the first letter of every word in the string capitliazed
def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"

# write a function called find_factors which acepts a number and returns a list of all the numbers which are divisible by starting form 1 and going up to the number
print("***********find_factors")
def find_factors(num):
  divisor_list = []
  for divisor in range(1, num+1):
    if num % divisor == 0:
      divisor_list.append(divisor)
  return divisor_list


print(find_factors(10)) # [1,2,5,10 ]
print(find_factors(11)) # [1,11]
print(find_factors(111)) # [1,3,37,111 ]
print(find_factors(321421)) # [1,293,1097,321421 ]
print(find_factors(412146)) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]

print("****************Includes")

# write a function called includes which accepts a collection, a value, and an optional starting index. the fucntions should return True if the value exists in the
# collection when we search from the starting index. Otherwise, it should return False.
# The collection can be a string a list or a dict, if the collection is a string ro array the third param is a starting index for where to search from. if the collectionis
# is a dict the funcion searchs for the value among values in the dict since objecst have no sort order the third param is ignored

def includes(item,val,start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]

includes([1, 2, 3], 1) # True
includes([1, 2, 3], 1, 2) # False
includes({ 'a': 1, 'b': 2 }, 1) # True
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False