import random

rand = random.randint(1,10)

# usr_inp = int(input("Please guess the number between 1 to 10: "))
# while usr_inp != rand:
# 	if usr_inp < rand:
# 		print("your guess is low, please try again!")
# 	else:
# 		print("your guess is high, please try again!")
# 	usr_inp = int(input())
# print("Nice Guess, It's CORRECT !!! \U0001f600")

#Refactored Code:

usr_inp = None
while usr_inp != rand:
	usr_inp = int(input("Please guess the number between 1 to 10: "))
	if usr_inp < rand:
		print("your guess is low, please try again!")
	elif usr_inp > rand:
		print("your guess is high, please try again!")
	else:
		print("Nice Guess, It's CORRECT !!! \U0001f600")
