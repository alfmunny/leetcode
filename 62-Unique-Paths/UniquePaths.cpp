#include <iostream>
#include <vector>
using namespace std;

class UniquePaths {
public:
    int UniquePathsTwoDim(int m, int n)
    {
        vector<vector<int>> dp(m, vector<int>(n, 1));
        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
            {
                dp[i][j] = dp[i - 1][j] + dp[j - 1][i];
            }

        return dp[m - 1][n - 1];
    }

    int UniquePathsOneDim(int m, int n) 
    {
        vector<int> dp(n, 1);
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }
};