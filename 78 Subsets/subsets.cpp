#include "subsets.h"
#include <iostream>

vector<vector<int>> Solution::subsets(vector<int>& nums)
{
    
    vector<vector<int>> ret = recursiveSubsets(nums, 0, nums.size() - 1);
    return ret;
}

vector<vector<int>> Solution::recursiveSubsets(vector<int>& nums, int start, int end)
{
    if(start == end)
        return vector<vector<int>>(1, vector<int>(1, nums[start]));

    vector<vector<int>> ret(1, vector<int>(1, nums[start]));

    for (vector<int> x : recursiveSubsets(nums, start + 1, end))
        {
            ret.push_back(x);
            x.push_back(nums[start]);
            ret.push_back(x);
        }

    return ret;
}
