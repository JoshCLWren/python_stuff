# Regular Expressions
# a way of describing patterns withing search strings

# validating emails

# starts with 1 or more letters,numbers,+,_,-,. thne
# a single @ sign then
# 1 or more letter, number, or - then
#  a single dot then
#  ends with 1 or more letter, number, -, or .

# (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

# \d - digit 0-9
# \w - letter digit or underscore
# \s - whitespace character
# \D - not a digit
# \W - not a word character
# \S - not a whitespace character
# . - any character except line break

# quantifiers
# + - one more time
# {3} - exactly x more times (3 more times)
# {3,5} - three to five more times
# {4,} - four or more times
# * - zero or more times
# ? - oncer or none (optional)

# character classes
# matches ranges and custom groups
# [] - matches any thing in the brackets
# [a-z] - matches all lower case letters for example
# [^0-9aeiou] - carrot means not inside brackets, this would only match consonants and special chars

# anchors and boundaries
# ^ - start of string or line
# $ - end of string or line
# \b - word boundary

# logical or (pipe)
# | - or

# Re Module
import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')#use the compile method and the regex as a raw string so we can use backslashes
res = pattern.search('Call me at 415 555-4242!')# returns a match object if the pattern is a match for the regex only returns one
print(res.group())#returns the match with the group method

res2 = pattern.findall('Call me at 415 555-4242 or 405 737-7502!')#reterns a list
print(res2)

def extract_all_phone(input):
  phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
  return phone_regex.findall(input)

print(extract_all_phone("my number is 392 323-1923"))

def is_valid_phone(input):
  phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
  match = phone_regex.fullmatch(input)
  if match:
    return True
  else:
    return False

print(is_valid_phone("456 546-4654"))

def is_valid_time(input):
  pattern = re.compile(r'^\d\d?:\d\d$')
  match = pattern.search(input)
  if match:
    return True
  return False

def parse_bytes(input):
  pattern = re.compile(r'[01]{8}')
  match = pattern.findall(input)
  if match:
    return match
  else:
    return None

# symbolic group names

def parse_name(input):
  # use ?P<inser_name_here> to give a portion of the regex a group symbol
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))

print(parse_name("Mrs. Tilda Swinton"))

def parse_date(string):
  date_regex = re.compile(r'^(?P<D>\d\d)[,/.](?P<m>\d\d)[,/.](?P<y>\d{4})$')
  match = date_regex.search(string)
  if match:
    return {
      "d": match.group("D"),
      "m": match.group("m"),
      "y": match.group("y")
    }
  return None

print(parse_date("12,04,2003"))

# compilation flags
# ignore case and verbose
# pattern = re.compile(r"""
# 	^([a-z0-9_\.-]+)	#first part of email
# 	@					#single @ sign
# 	([0-9a-z\.-]+)		#email provider
# 	\.					#single period
# 	([a-z\.]{2,6})$		#com, org, net, etc.
# """, re.X |)

# match = pattern.search("ThomaS123@Yahoo.com")
# print(match.group())
# print(match.groups())

# regex substitution basics
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow!"
# \g<group number> referers to which part of the regex you want to substitute
# group 1 is mr group two is first initial and group 3 is the rest of the last name
pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
results = pattern.sub("\g<1> \g<2>", text)

print(results)

def censor(input):
  pattern = re.compile(r'(fracking|frack)', re.I)
  return pattern.sub("CENSORED", input)

# swapping file names
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

# new output 1978 - Tales of the City
fixed_titles = []
titles.sort()
# print(titles)
pattern = re.compile(r'(^[\w ]+)\((\d{4})\)')
for book in titles:
  # we can use sub to switch around groups and even leave out chars like the parens
  result = pattern.sub("\g<2> - \g<1>", book)
  fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)


