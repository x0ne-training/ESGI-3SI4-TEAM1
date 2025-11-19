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

    def get_user_input(self):
        """Gets and processes the user's input."""
        command = input("Enter command (plant [x] [y], quit): ").lower().split()
        if not command:
            return
        if command[0] == "plant" and len(command) == 3:
            try:
                x, y = int(command[1]), int(command[2])
                self.place_plant(x, y)
            except ValueError:
                print("Invalid coordinates.")
        elif command[0] == "quit":
            self.game_over = True
        else:
            print("Invalid command.")

    def place_plant(self, x, y):
        """Places a plant on the board if the position is valid."""
        if not (0 <= x < 10 and 0 <= y < 5):
            print("Invalid coordinates.")
            return
        if any(plant.x == x and plant.y == y for plant in self.plants):
            print("A plant is already there.")
            return
        self.plants.append(Plant(x, y))

    def run(self):
        """The main game loop."""
        while not self.game_over:
            self.print_board()
            self.get_user_input()

if __name__ == "__main__":
    game = Game()
    game.run()
