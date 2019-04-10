#include <iostream>
#include <vector>
using std::vector;
using std::min;
using std::max;

class Solution {
    public:
        int maxArea(vector<int>& height) {
            int i = 0, j = height.size() - 1, ret = 0;
            int h = 0;
            while (i < j)
            {
                h = min(height[i], height[j]);
                ret = max(ret, h * (j - i));
                while(height[i] <= h && i < j) i++;
                while(height[j] <= h && i < j) j--;
            }

            return ret;
        }
};

int main() { return 0; }
