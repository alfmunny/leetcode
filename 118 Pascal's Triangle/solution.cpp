#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ret;
        if(numRows == 0)
            return ret;

        ret.push_back(vector<int>(1, 1));

        for(int i = 1; i < numRows; i++)
        {
            vector<int> tmp(i + 1, 1);
            for(int j = 1; j < (tmp.size()+1)/2; j++)
            {
                tmp[tmp.size() - 1 - j] = tmp[j] = ret[i - 1][j] + ret[i - 1][j - 1];
            }
            ret.push_back(tmp);
        }
        return ret;
    }
};
