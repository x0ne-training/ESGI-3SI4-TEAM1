# ... (keep existing code from commit 3)

# --- Main Game Logic ---
def main():
    """Main function to run the game."""
    board = create_board()
    game_objects = []
    
    while True:
        clear_screen()
        print_board(board, game_objects)
        
        # Get user input to place a plant
        try:
            plant_y = int(input(f"Enter row to plant (0-{BOARD_HEIGHT-1}): "))
            plant_x = int(input(f"Enter col to plant (0-{BOARD_WIDTH-1}): "))
            if 0 <= plant_y < BOARD_HEIGHT and 0 <= plant_x < BOARD_WIDTH:
                game_objects.append(Plant(plant_x, plant_y))
        except ValueError:
            print("Invalid input. Please enter a number.")

        time.sleep(1)

if __name__ == "__main__":
    main()
