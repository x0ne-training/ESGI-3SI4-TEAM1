import time
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function to run the game."""
    while True:
        print("Game running...")
        time.sleep(1)

if __name__ == "__main__":
    main()
