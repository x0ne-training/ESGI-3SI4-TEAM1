import time
import random

class Game:
    """Manages the game state and logic."""
    def __init__(self):
        self.board = [["." for _ in range(10)] for _ in range(5)]
        self.game_over = False

    def print_board(self):
        """Prints the current state of the game board."""
        for row in self.board:
            print(" ".join(row))
        print("-" * 20)

    def run(self):
        """The main game loop."""
        while not self.game_over:
            self.print_board()
            time.sleep(1)

if __name__ == "__main__":
    game = Game()
    game.run()
