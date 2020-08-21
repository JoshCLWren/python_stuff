# filter
# there is a lambda for each vlue in teh iterable
# returs filter object which can be convereted into other iterables
# the object contians only the values that return true to the lambda

l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, l))
# variable name = makes it  alist(filters(lambda anonyopmous function throway variabel designated each value of iterable: action to filter on is a boolean, iterable))
print(evens)

names = ['austin', 'penny', 'anthony', 'angel', 'billy']

a_names = list(filter(lambda n: n[0] =='a', names))
# returns only names that start with a
print(a_names)

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

usernames = list(map(lambda user: user["username"].upper(),
  filter(lambda u: not u['tweets'], users)))
# maps over the users object that has been filtered to usernames that don't have tweets and the returns those usernames capilatilized
print(usernames)

# list comprehension is the preffered method and can do it in a oneliner

usernames2 = [user["username"].upper() for user in users if not user["tweets"]]

print(usernames2)

numbers = [-1, 3, -44, 1]
def remove_negatives(nums):
  return list(filter(lambda n: n >= 0, nums))

print(remove_negatives(numbers))