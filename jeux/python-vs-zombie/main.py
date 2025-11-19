import time
import random

PLANT_COSTS = {"P": 100, "S": 50}
ZOMBIE_HEALTH = {"Z": 100, "B": 200}
PEASHOOTER_DAMAGE = 20
ZOMBIE_DAMAGE = 10
INITIAL_SUN = 150
SUNFLOWER_SUN_PRODUCTION = 25

class Plant:
    """Represents a plant on the board."""
    def __init__(self, plant_type, x, y):
        self.plant_type = plant_type
        self.x = x
        self.y = y
        self.health = 100

    def is_alive(self):
        return self.health > 0

class Zombie:
    """Represents a zombie on the board."""
    def __init__(self, zombie_type, y):
        self.zombie_type = zombie_type
        self.x = 9
        self.y = y
        self.health = ZOMBIE_HEALTH[zombie_type]

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
        self.sun = INITIAL_SUN
        self.turn = 0
        self.game_over = False

    def print_board(self):
        """Prints the current state of the game board."""
        print(f"Sun: {self.sun}")
        for y in range(5):
            row_str = ""
            for x in range(10):
                char_to_print = "."
                for plant in self.plants:
                    if plant.x == x and plant.y == y:
                        char_to_print = plant.plant_type
                        break
                for zombie in self.zombies:
                    if int(zombie.x) == x and zombie.y == y:
                        char_to_print = zombie.zombie_type
                        break
                row_str += f" {char_to_print} "
            print(row_str)
        print("-" * 30)

    def get_user_input(self):
        """Gets and processes the user's input."""
        command = input("Enter command (plant [P/S] [x] [y], quit): ").lower().split()
        if not command:
            return
        if command[0] == "plant" and len(command) == 4:
            plant_type = command[1].upper()
            try:
                x, y = int(command[2]), int(command[3])
                self.place_plant(plant_type, x, y)
            except ValueError:
                print("Invalid coordinates.")
        elif command[0] == "quit":
            self.game_over = True
        else:
            print("Invalid command.")

    def place_plant(self, plant_type, x, y):
        """Places a plant on the board if the position is valid and there is enough sun."""
        if plant_type not in PLANT_COSTS:
            print("Invalid plant type.")
            return
        if not (0 <= x < 10 and 0 <= y < 5):
            print("Invalid coordinates.")
            return
        if any(plant.x == x and plant.y == y for plant in self.plants):
            print("A plant is already there.")
            return
        if self.sun >= PLANT_COSTS[plant_type]:
            self.sun -= PLANT_COSTS[plant_type]
            self.plants.append(Plant(plant_type, x, y))
        else:
            print("Not enough sun.")

    def update_game_state(self):
        """Updates the state of all game objects for the current turn."""
        self.turn += 1
        # Sunflowers generate sun
        for plant in self.plants:
            if plant.plant_type == "S":
                self.sun += SUNFLOWER_SUN_PRODUCTION

        # Peashooters shoot
        for plant in self.plants:
            if plant.plant_type == "P":
                for zombie in self.zombies:
                    if zombie.y == plant.y and zombie.x > plant.x:
                        zombie.health -= PEASHOOTER_DAMAGE
                        break
        self.zombies = [z for z in self.zombies if z.is_alive()]

        # Zombies move and attack
        for zombie in self.zombies:
            zombie.move()
            for plant in self.plants:
                if int(zombie.x) == plant.x and zombie.y == plant.y:
                    plant.health -= ZOMBIE_DAMAGE
        self.plants = [p for p in self.plants if p.is_alive()]

        # Spawn new zombies
        if self.turn % 5 == 0:
            zombie_type = random.choice(list(ZOMBIE_HEALTH.keys()))
            y = random.randint(0, 4)
            self.zombies.append(Zombie(zombie_type, y))

        # Check for game over
        for zombie in self.zombies:
            if zombie.x < 0:
                self.game_over = True
                print("The zombies have reached your house! Game Over.")
                return

    def run(self):
        """The main game loop."""
        while not self.game_over:
            self.print_board()
            self.get_user_input()
            if not self.game_over:
                self.update_game_state()

if __name__ == "__main__":
    game = Game()
    game.run()
