#include "solution.h"

using namespace std;

 vector<int> Solution::findDuplicates(vector<int>& nums) {
        int n = nums.size();
        vector<int> counter(n+1, 0);
        vector<int> ret {};
        
        for( int i : nums)
        {
            counter[i]++;
            if (counter[i] == 2)
            {
                ret.push_back(i);
            }
        }
        return ret;
}