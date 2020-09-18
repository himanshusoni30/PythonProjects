"""
age = input("Please enter your age in years: ")
if age:
	age = int(age)
	if age >= 18 and age < 21:
		print("Please wear a wrist band.")
	elif(age >= 21):
		print("Normal Entry.")
	else:
		print("You are too young, SORRY NOT ALLOWED !!!")
else:
	print("Not a valid age...please enter a valid age.")
"""

#Simpler code with and or condition

age = input("Please enter your age in years: ")
if age:
	age = int(age)
	if age >= 21:
		print("Normal Entry.")
	elif age >= 18:		
		print("Please wear a wrist band.")
	else:
		print("You are too young, SORRY NOT ALLOWED !!!")
else:
	print("Not a valid age...please enter a valid age.")