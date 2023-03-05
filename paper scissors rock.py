import random
import easygui

null = 0

while True:
    weapons = ["Paper", "Scissors", "Rock"]
    computer = random.choice(weapons)

    play = easygui.buttonbox("Welcome to Rock, Paper, Scissors Do You Want to Play a Game?", "Welcome and Rules",
                             choices=["Yes", "No"])

    if play == "Yes":
        choice = easygui.buttonbox("Choose your Weapon!", "Choices", choices=(weapons[0], weapons[1], weapons[2]))
        easygui.msgbox(f"You chose {choice}, and the computer chose {computer}")

        if computer == choice:
            result = "This was a draw!"
        elif computer == "Paper" and choice == "Rock" or \
                computer == "Scissors" and choice == "Paper" or \
                computer == "Rock" and choice == "Scissors":
            result = "You Lose!"
        else:
            result = "You Win!"

        easygui.msgbox(f"{result}")

    elif play == "No":
        break
