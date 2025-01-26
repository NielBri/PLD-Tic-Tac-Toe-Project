# Program that can let you play tic tac toe

# Put the random function for the ai to use

import random

# Make a grid or place to play
grid = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

player = "X"
winner = None
gameRunning = True
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
def playerinput(grid):
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
def checkplaceHorizontal(grid):
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

def checkplaceVertical(grid):
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

def checkplaceDiagonal(grid):
    global winner
    if grid[0] == grid[4] == grid[8] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[2] == grid[4] == grid[6] and grid[2] != "-":
        winner = grid[2]
        return True

# Switching of players
def switchplayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

# Determining the Tie and Win
def checktie(grid):
    global gameRunning
    global ties
    if "-" not in grid and winner is None:
        print_grid(grid)
        print("Game Finished. Tie!")
        ties += 1
        gameRunning = False

def checkwinner():
    global gameRunning
    global player_o_wins
    global player_x_wins

    if checkplaceDiagonal(grid) or checkplaceVertical(grid) or checkplaceHorizontal(grid):
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
while gameRunning:
    print_grid(grid)

    checkwinner()
    if winner is not None:
        break

    checktie(grid)

    if mode == "1": # Player vs Player
        playerinput(grid)
    elif mode == "2":  # Player vs Bot
        if player == "X":
            playerinput(grid)
        else:
            bot_moves(grid)

    switchplayer()

# Player Scores!
print("Scores")
print("Player X wins: ", player_x_wins)
print("Player O wins: ", player_o_wins)
print("Ties: ", ties)
