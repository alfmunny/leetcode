#include <iostream>
#include <vector>

/* Recursive Solution */
class Solution1 {
    public:
        std::vector<int> memo;
        int robe(std::vector<int>& nums) {
            memo = std::vector<int>(nums.size(), -1);
            return robeRecursive(nums, nums.size() - 1);
        }

        int robeRecursive(std::vector<int>& nums, int n) {
            if (n<0) return 0;
            if (n>nums.size() - 1) return 0;

            if (memo[n]>=0) 
                return memo[n];
            else 
                memo[n] = std::max((robeRecursive(nums, n - 2) + nums[n]), robeRecursive(nums, n-1));
            return memo[n];
        }
};

/* Iterative Solution */

class Solution2 {
    public:
        int robe(std::vector<int>& nums) {
            int n = nums.size();

            if (n==0) return 0;

            int memo[n + 1];
            memo[0] = 0;
            memo[1] = nums[1];

            /* pay attention to the starting point of i */ 
            for (size_t i = 1; i < n; ++i) 
            {
                memo[i + 1] = std::max(memo[i - 1] + nums[i], memo[i]);
            } 

            return memo[n];
        }
};

int main() {
    Solution2 y;

    std::vector<int> nums{1,2,3,1};

    int ret = y.robe(nums);

    std::cout << ret;

    return 0;

}
