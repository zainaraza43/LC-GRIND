#include <stdio.h>
#include <stdlib.h>

int climbStairs(int n){
    int *DP = malloc(sizeof(int) * (n+1));
    
    for (int i = n; i >= 0; i--) {
        if (i == n || i == n-1) {
            DP[i] = 1;
        } else {
            DP[i] = DP[i+1] + DP[i+2];
        }
    }
    return DP[0];
}

//driver code
int main() {
    printf("%d", climbStairs(5));
}