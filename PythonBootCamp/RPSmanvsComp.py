import random
print("......rock.....")
print("......paper.....")
print("......scissors.....")
Human = input("Human choice: ").lower()
print()
Computer = random.randint(1,3) #1 - paper, 2 - rock, 3 - scissors

if Computer == 1:
	Computer = "paper"
	print("Computer chose: paper")
elif Computer == 2:
	Computer = "rock"
	print("Computer chose: rock")
elif Computer == 3:
	Computer = "scissors"
	print("Computer chose: scissors")

if Human == Computer:
	print("Match tied, no one wins !!!")
elif Human == "rock":
	if Computer == "scissors":		
		print("Human wins !!!")
	# elif Computer == "paper":	
	else:	
		print("Computer wins !!!")
elif Human == "paper" :
	if Computer == "scissors":
		print("Computer wins !!!")
	# elif Computer == "rock":	
	else:	
		print("Human wins !!!")
elif Human == "scissors":
	if Computer == "rock":
		print("Computer wins !!!")
	# elif Computer == "paper":
	else:
		print("Human wins !!!")
else:
	print("Something went wrong!!!")