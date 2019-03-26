#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int n = nums.size();

        vector<int> res = vector<int>(n, 1); 

        for(size_t i = 1; i < n; i++)
        {
           res[i] = res[i-1] * nums[i-1];
        }

        int right = 1;

        for(int i = n-1; i >= 0; i--)
        {
            res[i] *= right;
            right *= nums[i];
        }
        
        return res;
    }
};


int main() {
    vector<int> nums{1, 2, 3, 4};
    Solution x;

    for (auto i : x.productExceptSelf(nums))
    {
        cout << i << endl;
    }

    return 0;
}