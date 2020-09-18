import random
"""
usr_inp = None
flag = None

while flag != "n":	
	rand = random.randint(1,10)
	while usr_inp != rand:
		usr_inp = int(input("Please guess the number between 1 to 10: "))
		if usr_inp < rand:
			print("your guess is low, please try again!")
		elif usr_inp > rand:
			print("your guess is high, please try again!")
		else:
			print("Nice Guess, It's CORRECT !!! \U0001f600")	
	flag = input("Do you wish to continue? y or n: ")
print("Thanks for playing this Game!!!")
"""

#Refactored Code:

rand = random.randint(1,10)
usr_inp = None

while True:	
	usr_inp = int(input("Please guess the number between 1 to 10: "))
	if usr_inp < rand:
		print("your guess is low, please try again!")
	elif usr_inp > rand:
		print("your guess is high, please try again!")
	else:
		print("Nice Guess, It's CORRECT !!! \U0001f600")	
		flag = input("Do you wish to continue? y or n: ")	
		if flag == "y":
			rand = random.randint(1,10)
			usr_inp = None
		else:
			print("Thanks for playing this Game!!!")
			break