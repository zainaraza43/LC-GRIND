int hoursRequired(int* piles, int pilesSize, int k) {
    int hours = 0;
    for (int i = 0; i < pilesSize; ++i)
        hours += (piles[i] - 1) / k + 1;
    return hours;
}

int minEatingSpeed(int* piles, int pilesSize, int h) {
    int lo, m, hi;
    lo = hi = 1;
    for (int i = 0; i < pilesSize; ++i) hi = (piles[i] > hi ? piles[i] : hi);
    while (lo != hi) {
        m = (lo + hi) / 2;
        if (hoursRequired(piles, pilesSize, m) <= h)
            hi = m;
        else
            lo = m + 1;
    }
    return lo;
}