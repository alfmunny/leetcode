#include <vector>
using std::vector;

class Solution {
    public:
        bool canJump(vector<int>& nums) {
            int lastPos = nums.size() - 1;

            for (int i = nums.size() - 1; i >= 0; i--)
            {
                if ( i + nums[i] >= lastPos)
                {
                    lastPos = i;
                }
            }

            return lastPos == 0;
        }
};

int main() { return 0;}
