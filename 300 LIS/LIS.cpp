#include "LIS.h"
#include <iostream>
#include <algorithm>

int LIS::lengthOfLIS(vector<int>& nums)
{
    if (nums.size() <= 1)
    {
        return nums.size();
    }

    vector<int> dp(nums.size(), 1);
    int ret = 1;
    int maxLength = 1;

    for (size_t i = 0; i < nums.size(); i++)
    {
        maxLength = 1;
        for (int j = i - 1; j >= 0; j--)
        {
            if (nums[j] < nums[i])
            {
                maxLength = max(dp[j], maxLength);
                dp[i] = maxLength + 1;
                if (dp[i] > ret)
                    break;

            }
        }
        ret = max(ret, dp[i]);
    }
    return  ret;
}
