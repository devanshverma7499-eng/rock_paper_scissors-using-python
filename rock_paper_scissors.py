import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Choose rock, paper, or scissors: ").lower()

if user not in choices:
    print("Invalid choice!")

else:
    print("Computer chose:", computer)

    if user == computer:
        print("It's a draw!")

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")