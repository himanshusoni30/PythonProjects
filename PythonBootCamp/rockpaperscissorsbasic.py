player1 = input("Player1: Please enter either rock, paper or scissors ")
for i in range(15):
	print()
	print()
	print()
	print("***********Please do not cheat*********")
	print()
	print()
	print()
player2 = input("Player2: Please enter either rock, paper or scissors ")

if player1 != player2:
	if player1 == "rock" and player2 == "scissors":
		print("Player1 wins !!!")
	elif player1 == "rock" and player2 == "paper":
		print("Player2 wins !!!")
	elif player1 == "scissors" and player2 == "rock":
		print("Player2 wins !!!")
	elif player1 == "scissors" and player2 == "paper":
		print("Player1 wins !!!")
	elif player1 == "paper" and player2 == "scissors":
		print("Player2 wins !!!")
	elif player1 == "paper" and player2 == "rock":
		print("Player1 wins !!!")
else:
	print("Match tied, no one wins !!!")
	