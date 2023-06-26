#define AVG(a, b) ((a + b) / 2)

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int l, m, h, x;
    x = *matrixColSize;
    l = 0;
    h = matrixSize * x - 1;
    while (l != h) {
        m = AVG(l, h);
        if (target < matrix[m / x][m % x]) {
            h = m;
        } else if (target > matrix[m / x][m % x]) {
            l = m + 1;
        } else {
            l = m;
            break;
        }
    }
    return (matrix[l / x][l % x] == target);
}
