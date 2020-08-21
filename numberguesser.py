import random

random_number = random.randint(1,1000)  # numbers 1 - 1000

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

# guess = None
# i = 0
# while guess != random_number:
#   guess = input("Guess a number between 1 and 1000!")
#   guess = int(guess)
#   i += 1
#   if guess > random_number:
#     print("Too high! Guess again!")
#   elif guess < random_number:
#     print("Too low! Guess again!")
#   else:
#     print(f"Correct! in {i} guesses")
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()

print(result)