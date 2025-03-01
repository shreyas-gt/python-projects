import random 

opt = ("rock", "paper", "scissors")
run = True
while run:
    player = None
    computer = random.choice(opt)
    while player not in opt:
        player = input('enter your choice rock, paper, scissors: ')

    print("Player: ", player)
    print("Computer: ", computer)

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer =="scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("play again? (y/n): ") == 'y':
        run = False

print("Game Over!!")