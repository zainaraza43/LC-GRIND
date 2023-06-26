// sort in reverse order of position
// calculate arrival time of each
// the idea is, for each furthest starting point, each greater arrival time means there is a new, later fleet (if a less pos arrives before a greater pos, it will be part of the same fleet)

typedef struct fleet {
    int pos;
    double time;
} fleet;

int cmpfleet(const void* a, const void* b) {
    return ((fleet*)b)->pos - ((fleet*)a)->pos;
}

int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    fleet f[positionSize];
    for (int i = 0; i < positionSize; ++i)
        f[i] = (fleet){ position[i], (double)(target - position[i]) / speed[i] };
    qsort(f, positionSize, sizeof(fleet), cmpfleet);
    int fleets = 0;
    double time = 0.0f;
    for (int i = 0; i < positionSize; ++i) {
        if (f[i].time > time) {
            time = f[i].time;
            ++fleets;
        }
    }
    return fleets;
}