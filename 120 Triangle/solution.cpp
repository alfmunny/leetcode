#include "solution.h"

using namespace std;

 int Solution::minimunTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> dp(triangle.back());
        vector<int> ret {};
        
        for (int l = n - 2; l >= 0; l--)
        {
            for (int j = 0; j <= l; j++)
            {
                dp[j] = min(dp[j], dp[j+1]) + triangle[l][j]; 
            }
        }
        return dp[0];
}