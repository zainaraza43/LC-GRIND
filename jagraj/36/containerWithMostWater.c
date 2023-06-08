int max(int a, int b) { return a > b ? a : b; }

int min(int a, int b) { return a < b ? a : b; }

int maxArea(int *height, int heightSize) {
  int i = 0, j = heightSize - 1;

  int r = 0;
  while (i < j) {
    r = max(r, min(height[i], height[j]) * (j - i));

    if (height[i] < height[j]) {
      i++;
    } else {
      j--;
    }
  }
  return r;
}
