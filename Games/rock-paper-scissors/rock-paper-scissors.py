import random

user_w = 0
computer_w = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit the game: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_option = random.randint(0,2)
    computer_pick = options[random_option]

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_w += 1
        print("Your points:", user_w, "computer points:", computer_w)
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_w += 1
        print("Your points:", user_w, "computer points:", computer_w)
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_w += 1
        print("Your points:", user_w, "computer points:", computer_w)
    else:
        print("Computer won!")
        computer_w += 1
        print("Your points:", user_w, "computer points:", computer_w)

print("Good game!")    
      