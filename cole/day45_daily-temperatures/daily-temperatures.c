/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#define CACHESIZE 101

int lookup(int temperature, int cache[CACHESIZE]) {
    int min = 0;
    for (int i = temperature + 1; i < CACHESIZE; ++i) {
        if (cache[i] && (!min || cache[i] < min))
            min = cache[i];
    }
    return min;
}

int max(int a, int b) { return a > b ? a : b; } // faster than 

int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int* answer = (int*)calloc(temperaturesSize, sizeof(int));
    *returnSize = temperaturesSize;
    int cache[CACHESIZE] = { 0 };
    for (int i = temperaturesSize - 1; i >= 0; --i) {
        answer[i] = max(lookup(temperatures[i], cache) - i, 0);
        cache[temperatures[i]] = i;
    }
    return answer;
}
