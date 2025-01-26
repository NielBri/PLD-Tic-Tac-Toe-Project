# Program that can let you play tic tac toe

# Put the random function for the ai to use

import random

# Make a grid or place to play
grid = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

player = "X"
winner = None
game_running = True
mode = None

# Player Score Checking
player_x_wins = 0
player_o_wins = 0
ties = 0

# Visual representation of the play space or grid
def print_grid(grid):
    print("  " + grid[0] + " | " + grid[1] + " | " + grid[2])
    print("-------------")
    print("  " + grid[3] + " | " + grid[4] + " | " + grid[5])
    print("-------------")
    print("  " + grid[6] + " | " + grid[7] + " | " + grid[8])


# Detect player input
def player_input(grid):
    while True:
        if player == "X":
            inp = int(input("Player (X) please choose a number between 1-9 as represented in the grid: "))
        else:
            inp = int(input("Player (O) please choose a number between 1-9 as represented in the grid: "))
        if inp >= 1 and inp <= 9 and grid[inp-1] == "-":
            grid[inp-1] = player
            break
        else:
            if player == "X":
                print("Failure. Try agin Player (X)")
            else:
                print("Failure. Try agin Player (O)")
            print_grid(grid)


# Check whether there is a tie or winner
def check_place_horizontal(grid):
    global winner
    if grid[0] == grid[1] == grid[2] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[3] == grid[4] == grid[5] and grid[3] != "-":
        winner = grid[3]
        return True
    elif grid[6] == grid[7] == grid[8] and grid[6] != "-":
        winner = grid[6]
        return True

def check_place_vertical(grid):
    global winner
    if grid[0] == grid[3] == grid[6] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[1] == grid[4] == grid[7] and grid[1] != "-":
        winner = grid[1]
        return True
    elif grid[2] == grid[5] == grid[8] and grid[2] != "-":
        winner = grid[2]
        return True

def check_place_diagonal(grid):
    global winner
    if grid[0] == grid[4] == grid[8] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[2] == grid[4] == grid[6] and grid[2] != "-":
        winner = grid[2]
        return True

# Switching of players
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

# Determining the Tie and Win
def check_tie(grid):
    global game_running
    global ties
    if "-" not in grid and winner is None:
        print_grid(grid)
        print("Game Finished. Tie!")
        ties += 1
        game_running = False

def check_winner():
    global game_running
    global player_o_wins
    global player_x_wins

    if check_place_diagonal(grid) or check_place_vertical(grid) or check_place_horizontal(grid):
        print(f"Winner is {winner}!!!!!!")
        if winner == "X":
            player_x_wins += 1
        elif winner == "O":
            player_o_wins += 1

def mode_select():
    global mode
    print("Please select game mode:")
    print("1. Player vs Player")
    print("2. Player vs AI")
    mode = input("Enter 1 or 2: ")

# Add AI for the game
def bot_moves(grid):
    print("Bot has made a move!")
    possible_moves = [i for i in range(len(grid)) if grid[i] == "-"]
    move = random.choice(possible_moves)
    grid[move] = player


# Check to see whether game is functioning whilst running
mode_select()
while True:
    # Add a mechanism that resets the board
    grid = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]

    player = "X"
    winner = None
    game_running = True

    while game_running:
        print_grid(grid)

        check_winner()
        if winner is not None:
            break

        check_tie(grid)

        if mode == "1": # Player vs Player
            player_input(grid)
        elif mode == "2":  # Player vs Bot
            if player == "X":
                player_input(grid)
            else:
                bot_moves(grid)
        else:
            print("Try again")
            mode_select()

        switch_player()

    # Player Scores!
    print("Scores")
    print("Player X wins: ", player_x_wins)
    print("Player O wins: ", player_o_wins)
    print("Ties: ", ties)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break