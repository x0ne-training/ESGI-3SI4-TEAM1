import time
import os

# --- Game Configuration ---
BOARD_WIDTH = 10
BOARD_HEIGHT = 5

# --- Utility Functions ---
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    """Creates an empty game board."""
    return [['.' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board):
    """Prints the current state of the game board."""
    for row in board:
        print(" ".join(row))

# --- Main Game Logic ---
def main():
    """Main function to run the game."""
    board = create_board()
    while True:
        clear_screen()
        print_board(board)
        time.sleep(1)

if __name__ == "__main__":
    main()
