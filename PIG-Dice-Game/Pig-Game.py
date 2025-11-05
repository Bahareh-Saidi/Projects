import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be 2-4 players")
    else:
        print("Invalid")

max_score = 50
player_score = [0 for x in range(players)]

while max(player_score) < max_score:
    for each_player in range(players):
        print("\nPlayer", each_player + 1, "turn has started\n")
        print("Your total score is:", player_score[each_player], "\n")
        
        current_score = 0

        while True:
            should_roll = input("Would Like to roll? (yes)").lower()
            if should_roll != "yes":
                break
            value = roll() 
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            print("Your score is:", current_score)

        player_score[each_player] += current_score
        print("Your total score is:", player_score[each_player])

max_score = max(player_score)
winning_index = player_score.index(max_score)
print("Player number", winning_index + 1, "is the winner with max score of", max_score)