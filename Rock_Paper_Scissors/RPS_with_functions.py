def get_player_choice(choices):
    import random
    print("here are your three options:")
    print(choices)
    
    our_choice = random.choice(choices)
    print(f"you chose {our_choice}.")
    return our_choice


def determine_who_wins(player_1_choice, player_2_choice):
    print("now we pick the winner.")
    print(f"Inside the judges booth: Player 1 chose: {player_1_choice}. Player 2 chose: {player_2_choice}.")
    if player_1_choice == player_2_choice:
        print("It was a tie game.")
        result = "result was a tie"
        return 

choices = ["Rock", "Paper", "Scissors"]


print('get player 1 choice')
player_1_choice = get_player_choice(choices)
print(f"Player 1 chose: {player_1_choice}.")

print('get player 2 choice')
player_2_choice = get_player_choice(choices)
print(f"Player 2 chose: {player_2_choice}.")

print('determine who wins')

winner = determine_who_wins(player_1_choice, player_2_choice)