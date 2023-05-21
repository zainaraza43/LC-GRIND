from typing import List


class Solution:
    def getBox(self, board, x, y):
        return [board[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]

    def removeDots(self, l):
        r = []
        for i in l:
            if i != ".":
                r.append(i)
        return r

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row = self.removeDots(row)
            if len(row) != len(set(row)):
                return False
        for i in range(9):
            col = self.removeDots([board[j][i] for j in range(9)])
            if len(col) != len(set(col)):
                return False

        for i in range(3):
            for j in range(3):
                box = self.removeDots(self.getBox(board, i * 3, j * 3))
                if len(box) != len(set(box)):
                    return False
        return True
