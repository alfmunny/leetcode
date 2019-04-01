#include <vector>
#include <iostream>

using std::vector;
using std::min;
using std::max;

class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int x = find_pivot(nums);
            std::cout << x << std::endl;

            if ( x == 0) return searchBinary(nums, target, 0, nums.size() - 1);
            else return max(searchBinary(nums, target, 0, x - 1), searchBinary(nums, target, x, nums.size() - 1));
        }

        int searchBinary(vector<int>& nums, int target, int left, int right) {
            int mid = (left+right)/2;

            if (right >= left)
            {
                if (target == nums[mid])
                {
                    return mid;
                }
                else if (target > nums[mid])
                {
                    return searchBinary(nums, target, mid+1, right);
                }
                else
                {
                    return searchBinary(nums, target, left, mid-1);
                }
            }
            return -1;
        }

        int find_pivot(vector<int>& nums) {
            for ( int i = 1; i < nums.size(); ++i) 
            {
                if (nums[i] < nums[i-1]) return i;
            }

            return 0;
        }
};

int main(int argc, const char *argv[])
{

    Solution x;
    vector<int> nums = { 4, 5, 6, 7, 0, 1, 2 };
    vector<int> nums1 = { 0, 1, 2, 3, 4, 5 };

    std::cout << x.search(nums, 0);

    return 0;
}
