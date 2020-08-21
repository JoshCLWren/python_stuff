# max
# returns the largestitem in an iterbale or the largest of two or more args

max(3,6,78,99) #returns 99

min(3,6,78,99) #retrurns 3

#works on strings or any othe riterable

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

print(min(len(name) for name in names))

#returns shortes length name "tim"

print(max(names, key=lambda n:len(n)))

# you can use a lambda and a key to sort by. This returns Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the title of the most played song
print(max(songs, key=lambda s: s['playcount'])['title']) #YMCA

def extremes(nums):
  return(min(nums), max(nums))