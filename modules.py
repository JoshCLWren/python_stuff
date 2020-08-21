# modules
# keeps python files small
#

from random import choice as pick, randint as magic_number_chooser
# alias names by using the as keyword
print(pick(["apple", "banana", "cherry", "durian"]))
print(magic_number_chooser(1,100))

# only use what you need.

# from random import choice, randint

import math

answer = math.sqrt(15129)

import keyword

def contains_keyword(*args):
  return any(keyword.iskeyword(arg) for arg in args)

contains_keyword("hello", "goodbye")