# [ __x__ for in __y__ in __z__]


nums = [1,2,3]

print([x*10 for x in nums])
# x what you want to do to each item in the list
# iteration of iterable
# list you are iteration over

# to do the same with a for loop you'd do:
numbers = [1,2,3,4,5]
doubled_numbers = []

for num in numbers:
  doubled_number = num * 10
  doubled_numbers.append(doubled_number)

print(doubled_numbers)
# this makes it to where you don't have to have a placeholder new array list variable and saves you the append and even for loop stuff cutting everything down to a one liner

name = 'colt'

print([char.upper() for char in name])

# conditional logic in list comprehnsions

evens = [num for num in numbers if num % 2 == 0]

odds = [num for num in numbers if num & 2 != 0]

print(evens)
print(odds)

multiply_evens_divide_odds = [num*2 if num & 2 == 0 else num/2 for num in numbers]

print(multiply_evens_divide_odds)

with_vowels = "This is so much fun!"
vowell_remover = "".join(char for char in with_vowels if char not in "aeiou")
print(vowell_remover)

lst1 = ["Ellie", "Tim", "Matt"]
# gets the first letter from each name
answer = [person[0] for person in lst1]
print(answer)

lst2 = [1,2,3,4,5,6]

answer2 = [num for num in lst2 if num % 2 == 0]

print(answer2)

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]

#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

answer = [num for num in range(1,100) if num % 12 == 0]

print(answer)

answer = [char for char in "amazing" if char not in "aeiou"]

print(answer)

# nested lists:
# put the first argument in brackets to make it multi dimensional.
answer = [[i for i in range(0,3)] for num in range(0,3)]

print(answer)

answer = [[i for i in range(0,10)] for num in range(0,10)]

print(answer)