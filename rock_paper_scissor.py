import random

#1 = rock
#2 = paper
#3 = scissor

computer = 0
human = 0

player = input("enter your name\n")
while True:
	number = random.randint(1,4)
	print('\nchoose one number\n1.rock\n2.paper\n3.scissor\n4.see scorecard\npress enter to exit')
	user_input = input("")

	
	if user_input == "":
		break


	elif int(user_input) == 4:
		print("\nscore is:\ncomputer = {}\n{} = {}\n".format(computer,player,human))


	elif int(user_input) == 1:
		if number == 1:
			print("you chose rock and computer also chose rock\ndraw")
			computer+=1
			human+=1

		elif number == 2:
			print("you chose rock and computer chose paper\ncomputer wins")
			computer+=1

		else:
			print("you chose rock and computer chose scissor\n{} wins".format(player))
			human+=1

	elif int(user_input) == 2:
		if number == 1:
			print("you chose paper and computer chose rock\n{} wins".format(player))
			human+=1

		elif number == 2:
			print("you chose paper and computer also chose paper\ndraw")
			computer+=1
			human+=1

		else:
			print("you chose paper and computer chose scissor\ncomputer wins")
			computer+=1


	else:
		if number == 1:
			print("you chose scissor and computer chose rock\ncomputer wins")
			computer+=1

		elif number == 2:
			print("you chose scissor and computer chose paper\n{} wins".format(player))
			human+=1

		else:
			print("you chose scissor and computer also chose scissor\ndraw")
			computer+=1
			human+=1

	print("\n[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]")