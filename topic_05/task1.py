import random

choices = ["stone", "scissor", "paper"]

player_choice = input("Enter your choice (stone, scissor, paper): ").lower()

if player_choice not in choices:
    print("Invalid choice! Please enter 'stone', 'scissor', or 'paper'.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "stone" and computer_choice == "scissor") or \
         (player_choice == "scissor" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "stone"):
        print("You win!")
    else:
        print("Computer wins!")
