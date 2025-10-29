PUZZLE = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],

    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],

    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9],
]

def _print_grid(grid):
    lines = []
    for r, row in enumerate(grid):
        if r % 3 == 0:
            lines.append("+-------+-------+-------+")
        line = []
        for c, v in enumerate(row):
            if c % 3 == 0:
                line.append("| ")
            line.append("." if v == 0 else str(v))
            line.append(" ")
        line.append("|")
        lines.append("".join(line))
    lines.append("+-------+-------+-------+")
    print("\n".join(lines))

def run_cli():
    print("=== Sudoku (Commit 1: affichage) ===")
    _print_grid(PUZZLE)
    print("Tape 'q' pour quitter.")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "q":
            print("Bye.")
            break

    
