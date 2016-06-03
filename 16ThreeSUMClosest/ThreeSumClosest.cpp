#include "ThreeSumClosest.h"
#include "../QuickSort/QuickSort.h"
#include <iostream>
#include <stdexcept>

int threeSumClosest(vector<int>& nums, int target)
{
    if (nums.size() < 3)
    {
        cerr << "Not enough elements in array" << endl;
        return NULL;
    }

    int len = nums.size();

    quickSort(nums, 0, len - 1);

    int head;
    int tail;
    int new_target;
    int sum;

    int res = nums[0] + nums[1] + nums[2];
    int diff = abs(res - target);
    int ndiff;

    // Notice the finishing point of the loop.
    // Do not loop for the last two element, it's a 3Sum problem. It's need at least 3 elements.
    for (size_t i = 0; i < len - 2; i++)
    {
        // begin from the next one 
        head = i + 1;
        // the last one of array
        tail = len - 1;

        while (head < tail)
        {

            sum = nums[i] + nums[head] + nums[tail];
            ndiff = abs(sum - target);

            // Solve it like a two sum problem
            if (ndiff == 0) return sum;
            else if (sum > target) tail--;
            else head++;
            
            // Remember the nearest one, 
            //Since it's not garanteed to find exact a 3Sum matches the target.
            if (ndiff < diff)
            {
                res = sum;
                diff = ndiff;
            }
        }
    }
    return res;
}

void test()
{
    vector<int> a = {2, 3, 2, -1, 1};

    int res = threeSumClosest(a, 1);
    cout << res << endl;
}
