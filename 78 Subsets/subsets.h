#pragma once
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums);

private:
    vector<vector<int>> recursiveSubsets(vector<int>& nums, int start, int end);
};