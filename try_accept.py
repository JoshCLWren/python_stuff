# THE BASIC SYNTAX:
# try:
# except:

# try:
#     foobar
# except:
#     print("PROBLEM!")
# print("after the try")

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return None
d = {"name": "Ricky"}
print(get(d, "city"))
d["city"]

# try:
# except:
# else:
# finally:


while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("Good job, you entered a number!")
		break
	finally:
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!")

# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")
