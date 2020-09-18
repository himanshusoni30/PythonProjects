player1 = input("Player1: Please enter either rock, paper or scissors ")
print("***********Please do not cheat********* \n\n\n" * 10)
player2 = input("Player2: Please enter either rock, paper or scissors ")

if player1 == player2:
	print("Match tied, no one wins !!!")
elif player1 == "rock":
	if player2 == "scissors":
		print("Player1 wins !!!")
	elif player2 == "paper":
		print("Player2 wins !!!")
elif player1 == "paper" :
	if player2 == "scissors":
		print("Player2 wins !!!")
	elif player2 == "rock":
		print("Player1 wins !!!")
elif player1 == "scissors":
	if player2 == "rock":
		print("Player2 wins !!!")
	elif player2 == "paper":
		print("Player1 wins !!!")
else:
	print("Something went wrong!!!")
	