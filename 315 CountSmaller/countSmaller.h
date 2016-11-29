#pragma once
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> ret(nums.size(), 0);
        vector<int> x = mergeSort(nums, ret, 0, nums.size() - 1);
        return x;
    }

    vector<int> mergeSort(vector<int>& nums, vector<int>& i_array,
        int start, int end)
    {
        int mid = (end - start) / 2;
        vector<int> ret(end - start + 1);
        int r = ret.size() - 1;

        if (start == end)
        {
            ret[start] = nums[start];
            return ret;
        }

        vector<int> left = mergeSort(nums, i_array, start, mid);
        vector<int> right = mergeSort(nums, i_array, mid+1, end);

        int i = left.size() - 1;
        int j = right.size() - 1;

        while ((i >= 0 || j >= 0) && r >= 0)
        {
            if (i < 0)
            {
                ret[r] = right[j];
                j--;
                r--;
            }
            else if ( j < 0)
            {
                ret[r--] = left[i];
                i--;
                r--;
            }
            else if (left[i] >= right[j])
            {
                ret[r--] = left[i];
                i--;
                r--;
            }
            else if (right[j] > left[i])
            {
                ret[r--] = right[j];
                j--;
                r--;
            }
        }

        return ret;
    }
};