#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res{};
        vector<int> temp{};

        find_backtrace(res, temp, candidates, target, 0);

        return res;

    }
private:
    void find_backtrace(
            vector<vector<int>>& combinationList, 
            vector<int>& combination, 
            vector<int>& candidates, 
            int target, 
            int start) 
    {
        if(target < 0) return;
        else if(target == 0) combinationList.push_back(combination);
        else 
        {
            for(size_t i = start; i < candidates.size(); i++)
            {
                combination.push_back(candidates[i]);
                find_backtrace(combinationList, combination, candidates, target - candidates[i], i); 
                combination.pop_back();
            }
        }

    }
};

int main() {
    vector<int> nums{2, 3, 6, 7};
    int target = 7;

    Solution x;
    for ( auto list : x.combinationSum(nums, target)) 
    {

        for ( auto num : list)
            cout << num << " ";
        cout << endl;
    }
    

    return 0;
}

