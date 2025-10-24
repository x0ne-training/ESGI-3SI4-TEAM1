
typedef struct {
    char value;
    int revealed; // 0 = cachee, 1 = visible
} Card;

void initBoard(Card board[SIZE][SIZE]);
void displayBoard(Card board[SIZE][SIZE]);
int isGameOver(Card board[SIZE][SIZE]);
void playGame(Card board[SIZE][SIZE]);

#endif
