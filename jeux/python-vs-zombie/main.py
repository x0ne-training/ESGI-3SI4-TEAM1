import time
import random

# Game constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 5
PLANT_TYPES = {"S": "Sunflower", "P": "Peashooter"}
PLANT_COSTS = {"S": 50, "P": 100}
PLANT_HEALTH = {"S": 50, "P": 100}
ZOMBIE_TYPES = {"Z": "Zombie", "B": "Buckethead Zombie"}
ZOMBIE_HEALTH = {"Z": 100, "B": 200}
ZOMBIE_SPEED = {"Z": 1, "B": 0.5}
ZOMBIE_DAMAGE = 10
PEASHOOTER_DAMAGE = 20
SUNFLOWER_SUN_PRODUCTION = 25
INITIAL_SUN = 150
ZOMBIE_SPAWN_RATE = 5  # Lower is faster

class Plant:
    """Represents a plant on the board."""
    def __init__(self, plant_type, x, y):
        self.plant_type = plant_type
        self.x = x
        self.y = y
        self.health = PLANT_HEALTH[plant_type]

    def is_alive(self):
        return self.health > 0

class Zombie:
    """Represents a zombie on the board."""
    def __init__(self, zombie_type, y):
        self.zombie_type = zombie_type
        self.x = BOARD_WIDTH - 1
        self.y = y
        self.health = ZOMBIE_HEALTH[zombie_type]
        self.speed = ZOMBIE_SPEED[zombie_type]
        self.last_move_time = time.time()

    def is_alive(self):
        return self.health > 0

    def move(self):
        current_time = time.time()
        if current_time - self.last_move_time >= 1 / self.speed:
            self.x -= 1
            self.last_move_time = current_time

class Game:
    """Manages the game state and logic."""
    def __init__(self):
        self.board = [["." for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.plants = []
        self.zombies = []
        self.sun = INITIAL_SUN
        self.turn = 0
        self.game_over = False

    def print_board(self):
        """Prints the current state of the game board."""
        print(f"Turn: {self.turn} | Sun: {self.sun}")
        for y in range(BOARD_HEIGHT):
            row_str = ""
            for x in range(BOARD_WIDTH):
                is_plant = False
                for plant in self.plants:
                    if plant.x == x and plant.y == y:
                        row_str += f" {plant.plant_type} "
                        is_plant = True
                        break
                if not is_plant:
                    is_zombie = False
                    for zombie in self.zombies:
                        if int(zombie.x) == x and zombie.y == y:
                            row_str += f" {zombie.zombie_type} "
                            is_zombie = True
                            break
                    if not is_zombie:
                        row_str += " . "
            print(row_str)
        print("-" * (BOARD_WIDTH * 3))

    def get_user_input(self):
        """Gets and processes the user's input."""
        command = input("Enter command (plant [S/P] [x] [y], wait, quit): ").lower().split()
        if not command:
            return
        if command[0] == "plant" and len(command) == 4:
            plant_type = command[1].upper()
            try:
                x, y = int(command[2]), int(command[3])
                self.place_plant(plant_type, x, y)
            except ValueError:
                print("Invalid coordinates.")
        elif command[0] == "wait":
            return
        elif command[0] == "quit":
            self.game_over = True
        else:
            print("Invalid command.")

    def place_plant(self, plant_type, x, y):
        """Places a plant on the board if the position is valid and there is enough sun."""
        if plant_type not in PLANT_TYPES:
            print("Invalid plant type.")
            return
        if not (0 <= x < BOARD_WIDTH and 0 <= y < BOARD_HEIGHT):
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
                        break  # Peashooter shoots the first zombie in its lane

        # Zombies move and attack
        for zombie in self.zombies:
            zombie.move()
            for plant in self.plants:
                if int(zombie.x) == plant.x and zombie.y == plant.y:
                    plant.health -= ZOMBIE_DAMAGE

        # Remove dead plants and zombies
        self.plants = [plant for plant in self.plants if plant.is_alive()]
        self.zombies = [zombie for zombie in self.zombies if zombie.is_alive()]

        # Spawn new zombies
        if self.turn > 0 and self.turn % ZOMBIE_SPAWN_RATE == 0:
            zombie_type = random.choice(list(ZOMBIE_TYPES.keys()))
            y = random.randint(0, BOARD_HEIGHT - 1)
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
