#include <iostream>
#include <vector>
using namespace std;

class MaximumSubArray {
public:
    int maxSubArray(vector<int>& nums) {
        int curMax = nums[0];
        int preMax = nums[0];
        for(size_t i = 1; i < nums.size(); i++)
        {

            preMax = max(preMax + nums[i], nums[i]);
            curMax = max(preMax, curMax);
        }
        return curMax;
    }
};


int main() {
    vector<int> vec{-1, -2, 1, 2, 5, -7, 2, 4, 5};
    MaximumSubArray solution;
    cout << solution.maxSubArray(vec) << endl;
    return 0;
}



