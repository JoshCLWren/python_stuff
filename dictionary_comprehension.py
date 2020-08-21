# dictionary comprehension

# similar syntax than list comprehension except fro brackets and the colon in the first arg {__:__ for ___ in ___}
# iterates over keys by default
#  to iterate over keys and values use .items()

numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key, value in numbers.items()}

print(squared_numbers)

print({num: num ** 2 for num in [1,2,3,4,5]})

str1 = "ABC"
str2 = "123"

combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)

# conditiona logic with dictionaires

num_list = [1,2,3,4]

# all the even and odd parites for the first million numbers
print({num:("even" if num % 2 == 0 else "odd") for num in range(1,1000000)})