import time
import random

class Plant:
    """Represents a plant on the board."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = "P"

class Game:
    """Manages the game state and logic."""
    def __init__(self):
        self.board = [["." for _ in range(10)] for _ in range(5)]
        self.plants = []
        self.game_over = False

    def print_board(self):
        """Prints the current state of the game board."""
        for y in range(5):
            row_str = ""
            for x in range(10):
                char_to_print = "."
                for plant in self.plants:
                    if plant.x == x and plant.y == y:
                        char_to_print = plant.char
                        break
                row_str += f" {char_to_print} "
            print(row_str)
        print("-" * 30)

    def run(self):
        """The main game loop."""
        # Example plant
        self.plants.append(Plant(2, 2))
        while not self.game_over:
            self.print_board()
            time.sleep(1)

if __name__ == "__main__":
    game = Game()
    game.run()
