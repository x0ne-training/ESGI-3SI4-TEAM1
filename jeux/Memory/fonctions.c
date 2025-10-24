
        if(board[x1][y1].value == board[x2][y2].value) {
            printf("Bravo! C'est une paire!\n");
        } else {
            printf("Pas de chance.\n");
            board[x1][y1].revealed = 0;
            board[x2][y2].revealed = 0;
        }

        printf("\n");
    }

    printf("Felicitation! Vous avez trouve toutes les paires!\n");
}
