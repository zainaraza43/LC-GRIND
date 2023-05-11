#include <stdio.h>
#include <stdlib.h>

int minCostClimbingStairs(int* cost, int costSize){
    for (int i = costSize-1; i >= 0; i--) {
        if (i == costSize-1 || i == costSize-2) {
            cost[i] = cost[i];
        } else {
            int oneJump = cost[i] + cost[i+1];;
            int twoJump = cost[i] + cost[i+2];
            cost[i] = oneJump < twoJump ? oneJump : twoJump;
        }
    }
    int minCost = cost[0] < cost[1] ? cost[0] : cost[1];
    return minCost;
}

//driver code
int main() {
    int costs[] = {10, 15, 20};
    printf("%d", minCostClimbingStairs(costs, 3));
}