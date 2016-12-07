#include "3Sum.h"

vector<vector<int>> Solution::threeSum(vector<int>& nums)
{
    vector<vector<int>> ret;
    sort(nums.begin(), nums.end());
    if(nums.size() < 3) return ret;
    
    for(int i = 0; i < nums.size() - 2; ++i)
    {
        if(i > 0 && nums[i] == nums[i-1]) continue;
        int start = i+1;
        int end = nums.size() - 1;
        while(start<end)
        {
            int sum = nums[start] + nums[end] + nums[i];
            if(sum == 0)
            {
                ret.push_back(vector<int>{nums[start], nums[end], nums[i]});
                --end;
                while(nums[end] == nums[end+1]) --end;
                ++start;
                while(nums[start] == nums[start-1]) ++start;
            }
            else if(sum > 0) --end;
            else ++start;
        }
    }
    return ret;
}
