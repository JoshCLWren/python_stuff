# Sorted
# returns a new sorted from the items in iterable

# sorted works on anythig that is iterable

more_numbers = [6,1,8,2]

sorted(more_numbers) #returns a new list but with sort!

print(more_numbers) #more_numbers is unchanged

print(sorted(more_numbers))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

print(sorted(users,key=lambda user: user['username']))
# sorts the users dictionary by the key which is a lmbda that is looking at the value of username. Retruns the dict in alpha
print(sorted(users,key=lambda user: len(user['tweets']), reverse=True))
# sorts the users dictionary by length of tweets in descending order