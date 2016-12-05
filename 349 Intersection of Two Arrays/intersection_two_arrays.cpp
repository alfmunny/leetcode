#include <iostream>
#include "intersection_two_arrays.h"

vector<int> Solution::intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> map;
        for(int i = 0; i < nums1.size(); i++)
        {
            if(map.count(nums1[i]) == 0)
                map[nums1[i]] = 1;
        }
        
        vector<int> ret;
        for(int j = 0; j < nums2.size(); j++)
        {
            if(map.count(nums2[j]) != 0)
            {
                ret.push_back(nums2[j]);
                map.erase(nums2[j]);
            }
        }
        return ret;
}