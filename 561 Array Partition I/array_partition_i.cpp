#include <iostream>
#include <vector>
using namespace std;

class ArrayParitionI {

public:
    int arrayPairSum(vector<int>& nums) {
        int ret = 0;

        sort(nums.begin(), nums.end());

        for (size_t i = 0; i < nums.size(); i += 2)
            ret += nums[i];

        return ret;
    }
};

int main() 
{
    vector<int> x{1, 2, 3, 4, 5, 6};

    ArrayParitionI solution;

    std::cout << solution.arrayPairSum(x) << std::endl;
}

