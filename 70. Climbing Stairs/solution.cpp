#include <iostream>

class Solution {
    public:
        int climbStairs(int n) {
            if (n == 1 || n == 2) return n;
            int prev1 = 1, prev2 = 2, ret;
            for (size_t i = 0; i < n - 2; ++i)
            {
                ret = prev1+prev2;
                prev1 = prev2;
                prev2 = ret;
            }
            return ret;
        }
};

int main()
{
    return 0;
}
