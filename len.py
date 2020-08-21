# len
# "length of something"


x = len('hello world')

print(x)

'hello'.__len__

class SpecialList:

  def __init__(self, data):
    self.__data = data

  def __len__(self):
    return 50 # len will always return 50 because it was overwritten this way

l1 = SpecialList([1,40,30,100])
l2 = SpecialList([])
print(len(l1))

print(len(l2))