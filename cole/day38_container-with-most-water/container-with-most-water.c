#define MIN(a, b) ( a < b ? a : b )
#define MAX(a, b) ( a > b ? a : b )
#define AREA(ct) ( (b - a) * MIN(height[b], height[a]) )

int maxArea(int* height, int heightSize) {
    int a = 0, b = heightSize - 1, v = 0;
    while (a < b) {
        v = MAX(v, AREA(cur));
        if (height[a] < height[b]) ++a; else --b;
    }
    return v;
}
