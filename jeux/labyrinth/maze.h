#ifndef MAZE_H
#define MAZE_H

typedef struct {
    int rows, cols;
    char **grid;
    int exitX, exitY;
} Maze;

void generateMaze(Maze *m, int rows, int cols);
void displayMaze(Maze *m, void *player);
void freeMaze(Maze *m);

#endif
