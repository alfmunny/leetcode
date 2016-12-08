#include "intersection_two_arrays2.h"

vector<int> Solution::intersect(vector<int>& nums1, vector<int>& nums2)
{
    unordered_map<int, int> map1;
    unordered_map<int, int> map2;
    
    for(int x : nums1)
    {
        ++map1[x];
    }
    
    for(int x : nums2)
    {
        ++map2[x];
    }
    
    vector<int> ret;
    
    for(auto & x : map1)
    {
        if(map2.count(x.first) > 0)
        {
            int val = std::min(map2[x.first], x.second);
            
            for(int i = 0; i < val; ++i)
            {
                ret.push_back(x.first);
            }
        }
    }
    return ret;
}
