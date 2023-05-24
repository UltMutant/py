import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
print("\n\tYou've only ",round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
count = 1
while count < math.log(upper - lower + 1, 2):
	count += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
		print("Congratulations you did it in ",
			count-1, " tries")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)