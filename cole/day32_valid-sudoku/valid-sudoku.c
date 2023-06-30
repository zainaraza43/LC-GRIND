#define SIZE 9

bool validnine(char n[SIZE]){
    bool c[SIZE] = {false};
    for (int i = 0; i < SIZE; ++i){
        if (n[i] == '.') continue;
        if (c[n[i] - '1']) return false;
        c[n[i] - '1'] = true;
    }
    return true;
}

bool isValidSudoku(char** board, int boardSize, int* boardColSize){
    char n[SIZE];
    // horizontal
    for (int i = 0; i < SIZE; ++i){
        memcpy(n, board[i], SIZE * sizeof(char));
        if (!validnine(n)) return false;
    }
    // vertical
    for (int i = 0; i < SIZE; ++i){
        for (int j = 0; j < SIZE; ++j) n[j] = board[j][i];
        if (!validnine(n)) return false;
    }
    // groups in the order:
    // 123
    // 456
    // 789
    for (int i = 0; i < SIZE; i += 3){                     // board ymin of sub box
        for (int j = 0; j < SIZE; j += 3){                 // board xmin of sub box
            for (int y = 0; y < 3; ++y){                   // sub box y
                for(int x = 0; x < 3; ++x){                // sub box x
                    n[x + (3 * y)] = board[i + y][j + x];
                }
            }
            if (!validnine(n)) return false;
        }
    }
    return true;
}