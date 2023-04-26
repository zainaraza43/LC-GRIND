#include <stdio.h>

int search(int* nums, int numsSize, int target){
  if (!numsSize) {
    return -1;
  }
  int l = 0, r = numsSize - 1;

  while (l<=r) {
    int m = (l + r) / 2;
    if (nums[m] == target) {
      return m;
    }
    if (target > nums[m])
      l = m + 1;
    else
      r = m - 1;
  }
  return -1;
}

int main() {
  int nums1[] = {-1, 0, 3, 5, 9, 12}, target1 = 9;
  int nums2[] = {-1, 0, 3, 5, 9, 12}, target2 = 4;
  int nums3[] = {}, target3 = 0;
  int nums4[] = {5}, target4 = 5;

  printf("%d\n", search(nums1, sizeof(nums1) / sizeof(nums1[0]), target1));
  printf("%d\n", search(nums2, sizeof(nums2) / sizeof(nums2[0]), target2));
  printf("%d\n", search(nums3, sizeof(nums3) / sizeof(nums3[0]), target3));
  printf("%d\n", search(nums4, sizeof(nums4) / sizeof(nums4[0]), target4));
}
