# Reading Files
# you can read a file with the open functin
# open returns a file object to you
# you can read a file object with the read method
# open has a lot of params but the only required one is file
# if file can't be opened an error will be raised
file = open("story.txt")
print(file.read())
# Python read files by using a cursor. If no value is set for read it defaults to -1 and reads the whole file and the cursor is at the end
# read will pick back up with where it was reading as the cursor placement if the file is changed
file.seek(0) #resets cursor to the n place
file.readline() #reads line by line and puts the cursor at the beginning of the next line
file.readlines() #returns a list of lines seperated by the lines. cursor will get moved to the end of file
file.close() #once closed it can't be read again until it's opened

# with blocks
with open("story.txt") as f: #this syntax automatically closes the file at the end of the with block
  data = f.read()
  print(data)

f.closed #True

# writing to text files
# you still have to open the file
# need to specify the "w" flag as the second arg
with open("haiku.txt", "w") as file:
  file.write("Writing files is great\n")
  file.write("Here's another line of text\n")
  file.write("Closing now, goodbye!\n")

# modes for opening files
# r read a file this is default
# w write t0a file - overwrites
# a append to a file only sticks it to the end
#  r+ read and write to a file - adds to the beginning of the file by default.

with open("haiku.txt", "r+") as f:
  f.write(":)")
  f.seek(10)
  f.write(":(")

# def copy(file_name, new_file_name):
#   with open(file_name) as file1:
#     text = file1.read()
#   with open(new_file_name, "w") as new_file:
#     new_file.write(text)

# def copy_and_reverse(file_name, new_file_name):
#   with open(file_name) as file1:
#     text = file1.read()
#   with open(new_file_name, "w") as new_file:
#     new_file.write(text[::-1])

# def statistics(file_name):
#   with open(file_name) as file1:
#     lines = file1.readlines()

#   return { "lines": len(lines), "words": sum(len(line.split(" ")) for line in lines), "characters": sum(len(line) for line in lines) }

# print(statistics('alice.txt'))

def find_and_replace(file_name, word, new_word):
  with open(file_name, "r+") as file1:
    text = file1.read()
    new_text = text.replace(word, new_word)
    file1.seek(0)
    file1.write(new_text)
    file1.truncate()

find_and_replace('alice.txt', 'Alice', 'Colt')
