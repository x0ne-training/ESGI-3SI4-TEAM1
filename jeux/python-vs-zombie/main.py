import time
import random

PEASHOOTER_DAMAGE = 20

class Plant:
    """Represents a plant on the board."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = "P"
        self.health = 100

    def is_alive(self):
        return self.health > 0

class Zombie:
    """Represents a zombie on the board."""
    def __init__(self, y):
        self.x = 9
        self.y = y
        self.char = "Z"
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def move(self):
        self.x -= 1

class Game:
    """Manages the game state and logic."""
    def __init__(self):
        self.board = [["." for _ in range(10)] for _ in range(5)]
        self.plants = []
        self.zombies = []
        self.turn = 0
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
                for zombie in self.zombies:
                    if int(zombie.x) == x and zombie.y == y:
                        char_to_print = zombie.char
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

    def update_game_state(self):
        """Updates the state of all game objects for the current turn."""
        self.turn += 1
        # Peashooters shoot
        for plant in self.plants:
            if plant.char == "P":
                for zombie in self.zombies:
                    if zombie.y == plant.y and zombie.x > plant.x:
                        zombie.health -= PEASHOOTER_DAMAGE
                        break
        self.zombies = [z for z in self.zombies if z.is_alive()]

        # Zombies move
        for zombie in self.zombies:
            zombie.move()
        # Spawn new zombies
        if self.turn % 5 == 0:
            y = random.randint(0, 4)
            self.zombies.append(Zombie(y))

    def run(self):
        """The main game loop."""
        while not self.game_over:
            self.print_board()
            self.get_user_input()
            self.update_game_state()

if __name__ == "__main__":
    game = Game()
    game.run()
