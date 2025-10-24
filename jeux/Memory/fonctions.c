
void playGame(Card board[SIZE][SIZE]) {
    int x1, y1, x2, y2;

    while(!isGameOver(board)) {
        displayBoard(board);

        printf("Choisissez la premiere carte (ligne colonne) : ");
        scanf("%d %d", &x1, &y1);
        printf("Choisissez la deuxieme carte (ligne colonne) : ");
        scanf("%d %d", &x2, &y2);

        if(x1 == x2 && y1 == y2) {
            printf("Vous devez choisir deux cartes differentes!\n");
            continue;
        }

        board[x1][y1].revealed = 1;
        board[x2][y2].revealed = 1;

        displayBoard(board);
