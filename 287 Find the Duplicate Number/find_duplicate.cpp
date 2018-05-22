#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int p1 = nums[0];
        int p2 = nums[p1];

        while(nums[p1] != nums[p2])
        {
            p1 = nums[p1];
            p2 = nums[nums[p2]];
        }

        p1 = 0;

        while(nums[p1] != nums[p2])
        {
            p1 = nums[p1];
            p2 = nums[p2];
        }
        return nums[p1];
    }
};

int main() {
    vector<int> nums{1, 3, 4, 2, 2};

    Solution x;
    cout << x.findDuplicate(nums) <<endl;
    return 0;

}

