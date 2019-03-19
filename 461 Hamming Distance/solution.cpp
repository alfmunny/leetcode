#include <iostream>
#include <vector>

class Solution {
public:
    int hammingDistance(int x, int y) {
        int ret = 0;
        int z = x^y;
        while (z>0) {
            if (z%2) ++ret;
            z = z/2;
        }
        return ret;
    }
};

int main()
{
    Solution s;
    int x = 1;
    int y = 4;

    std::cout << s.hammingDistance(x, y) << std::endl;

}

