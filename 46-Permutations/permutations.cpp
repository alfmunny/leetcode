#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret;
        vector<int> temp;

        permute_recursive(ret, temp, nums, 0);

        return ret;
    }

private:
    void permute_recursive(vector<vector<int>>& permutationList, vector<int>& permutation, vector<int>& nums, int start) {

        if ( start == nums.size() ) {
            permutationList.push_back(permutation);
            return;
        }

        for(size_t i = start; i < nums.size();  i++)
        {
            permutation.push_back(nums[i]);
            permute_recursive(permutationList, permutation, nums, start);
            permutation.pop_back();
        }

    }

};

int main() {
    vector<int> nums{1, 2, 3};

    Solution x;
    for (auto list : x.permute(nums))
    {
        for( auto num : list)
            cout << num << " ";
        cout << endl;
    }

    return 0;
}

