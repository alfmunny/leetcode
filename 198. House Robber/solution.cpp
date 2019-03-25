#include <iostream>
#include <vector>

/* Recursive Solution */
class Solution1 {
    public:
        std::vector<int> memo;
        int rob(std::vector<int>& nums) {
            memo = std::vector<int>(nums.size(), -1);
            return robRecursive(nums, nums.size() - 1);
        }

        int robRecursive(std::vector<int>& nums, int n) {
            if (n<0) return 0;
            if (n>nums.size() - 1) return 0;

            if (memo[n]>=0) 
                return memo[n];
            else 
                memo[n] = std::max((robRecursive(nums, n - 2) + nums[n]), robRecursive(nums, n-1));
            return memo[n];
        }
};

/* Iterative Solution */

class Solution2 {
    public:
        int rob(std::vector<int>& nums) {
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

/* Iterative Solution without memory array*/

class Solution3 {
    public:
        int rob(std::vector<int>& nums) {
            int n = nums.size();

            if (n==0) return 0;

            int prev1 = 0;
            int prev2 = nums[0];
            int tmp = 0;

            /* pay attention to the starting point of i */ 
            for (size_t i = 1; i < n; ++i) 
            {
                tmp = std::max(prev1 + nums[i], prev2);
                prev1 = prev2;
                prev2 = tmp;
            } 

            return prev2;
        }
};

int main() {
    Solution3 y;

    std::vector<int> nums{1,2,3,1};

    int ret = y.rob(nums);

    std::cout << ret;

    return 0;

}
