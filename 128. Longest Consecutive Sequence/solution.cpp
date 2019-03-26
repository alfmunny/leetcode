#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>

class Solution {
    public:
        int longestConsecutive(std::vector<int>& nums) {
            std::unordered_map<int, int> m;
            int ret = 0;
            for (int n : nums) {
                if (m[n]) continue;
                else ret = std::max(ret, m[n] = m[n - m[n -1]] = m[n + m[n+1]] = m[n-1] + m[n+1] + 1);
            }
            return ret;
        }
};

int main() { 

    std::vector<int> nums = { 100,4,200,1,3,2 };
    Solution x;
    std::cout << x.longestConsecutive(nums);

    return 0;
}


