#include "QuickSort.h"

void quickSort(std::vector<int>& nums, int l, int r)
{
    // stop when the two pointers are at the same position
    if (l >= r)
    {
        return;
    }

    int head = l;
    int end = r;

    // use the first value as the middle value 
    int mark = nums[head];

    // don't forget to exclude this middle value for comparison
    l = head + 1;

    while (l < r)
    {
        // move the left pointer
        while (nums[l] < mark && l < r) l++;
        // move the right pointer
        while (nums[r] >= mark && l < r) r--;

        // swap the left and right 
        std::swap(nums[l], nums[r]);
    }
    
    // Notice: 
    // The right pointer and the left pointer will be at the same position.
    // So the value at this position hasn't been compared.
    // It musted be compared with the middle value and change it's position.

    // If the value is smaller than the middle value,
    // swap them
    if (nums[r] < mark)
    {
        std::swap(nums[r], nums[head]);
    }

    // Since the two pointers are at the same position, and the value is larger than the left side of the array.
    // so exclude it with r - 1
    quickSort(nums, head, r - 1);
    // But it's not for sure that this value is smaller than all the values of the right side.
    // so include it with l
    quickSort(nums, l, end);

    return;
}