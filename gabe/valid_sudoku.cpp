class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        char r, c, s;

        for(int i = 0; i < 9; i++) {
            set<char> rows, columns, squares;

            for(int j = 0; j < 9; j++) {
                r = board[i][j];
                c = board[j][i];
                s = board[j/3 + (i*3)%9][j % 3 + i / 3 * 3];

                if(r != '.' && !rows.insert(r).second) {
                    return false;
                }
                if(c != '.' && !columns.insert(c).second) {
                    return false;
                }
                if(s != '.' && !squares.insert(s).second) {
                    return false;
                }
            }
        }


        return true;
    }
};