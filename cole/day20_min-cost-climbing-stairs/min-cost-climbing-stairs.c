#define MIN(a, b) (a < b ? a : b)

int minCostStep(int step, int *cost, int costSize, int *cache){
    if (cache[step] >= 0) return cache[step];
    int b = minCostStep(step - 2, cost, costSize, cache);
    int a = minCostStep(step - 1, cost, costSize, cache);
    cache[step] = MIN(a, b) + cost[step];
    return cache[step];
}

int minCostClimbingStairs(int* cost, int costSize){
    int cache[costSize];
    memset(cache, 0xff, costSize * sizeof(int));
    memcpy(cache, cost, sizeof(int) * 2);
    int a = minCostStep(costSize - 1, cost, costSize, cache);
    int b = minCostStep(costSize - 2, cost, costSize, cache);
    return MIN(a, b);
}
