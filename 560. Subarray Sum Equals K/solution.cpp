#include <vector>
#include <iostream>
#include <unordered_map>
using std::vector;

// Solution 1: calculate every sum between two numbers, remember them in an array.
class Solution1 {
    public:
        int subarraySum(std::vector<int>& nums, int k) {

            int len = nums.size();
            std::vector<int> sums(len, 0);
            int ret = 0;
            if (nums[0] == k) ret++;
            sums[0] = nums[0];

            for(size_t i = 1; i < len; ++i)
            {
                sums[i] = nums[i] + sums[i-1];

                if (sums[i] == k) ret++;
            }

            for(size_t i = 1; i < len ; ++i)
            {
                for(size_t j = i; j < len; ++j)
                {
                    sums[j] = sums[j] - sums[i-1];
                    if (sums[j] == k) ret++;
                }
            }

            return ret;
        }

};

class Solution2 {
    public:
        int subarraySum(vector<int>& nums, int k)
        {
            int ret = 0, sum = 0;
            std::unordered_map<int, int> hash;
            hash[0] = 1;
            for ( size_t i = 0; i < nums.size(); ++i ) {
                sum += nums[i];
                if (hash.find(sum - k) != hash.end()) ret += hash[sum - k];
                hash[sum]++;
            }

            return ret;
        }
};

int main() {
    Solution2 x;
    std::vector<int> nums = { 0,0,0,0,0,0,0,0,0,0};
    int res = x.subarraySum(nums, 0);
    std::cout << res << std::endl;
    return 0;
}
