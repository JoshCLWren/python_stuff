# zip
# makes an iterator that aggregates elements from each of the iterables
# retruns an iterator of tuples wher i-th tuple contaings the i-th element from each of the args

# zips to lists together

first_zip = zip([1,2,3],[4,5,6])

list(first_zip) # [(1,4),(2,5),(3,6)]
dict(first_zip) # {1:4, 2:5, 3:6}

# goes from left to right, it stops as soon as the shortest iterator stops
# can use the star operator

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

final_grades = {pair[0]:max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}

print(final_grades)
grades = zip(
  students,
  map(
    lambda pair: max(pair),
    zip(midterms, finals)
  ))


print(dict(grades))

def interleave(str1, str2):
  return "".join("".join(x) for x in (zip(str1, str2)))

def triple_and_filter(nums):
  return list(map(lambda num: num*3,
  filter(lambda num: num % 4 == 0, nums)))


triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]

