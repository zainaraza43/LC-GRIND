#include<stdio.h>
#include<stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize){
    int *returnArray = malloc(sizeof(int) * (n+1));
    int offset = 1;
    returnArray[0] = 0;

    for (int i = 1; i < n + 1 ; i++) {
        if (i == offset * 2) {
            offset = i;
        }
        returnArray[i] = 1 + returnArray[i - offset];
        printf("%d\n", returnArray[i]);
    }

    *returnSize = n + 1;
    return returnArray;
}

int main() {
    int n = 5;
    int returnSize = 6;
    int * returnArray = countBits(n, &returnSize);

    for (int i = 0; i < n + 1; i++) {
        printf("%d\n", returnArray[i]);
    }
}