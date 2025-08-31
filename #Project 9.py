#In this game, the computer always chooses a number that makes the total a multiple of 4.
#This strategy ensures that if the player does not make a mistake, the computer will always win. Enjoy playing!
def game_21():
    total = 0

    while total < 21:
        # Player's turn
        player_input = int(input("Enter a number between 1 and 3: "))
        while player_input < 1 or player_input > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            player_input = int(input("Enter a number between 1 and 3: "))
        total += player_input
        print(f"Player's turn: {player_input}. Total is now {total}.")
        if total >= 21:
            print("Computer wins!")
            break

        # Computer's turn
        computer_input = 4 - player_input
        total += computer_input
        print(f"Computer's turn: {computer_input}. Total is now {total}.")
        if total >= 21:
            print("Player wins!")

# Start the game
game_21()
