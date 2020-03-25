#include <iostream>
#include <vector>
using namespace std;

class UniquePathsII {
public:
    int UniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.size() == 0)
        {
            return 0;
        }
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        vector<vector<int>> dp(m, vector<int>(n, 1));

        int flag = 0;

        for (int i = 0; i < m; i++)
        {
            if (obstacleGrid[i][0] == 1)
            {
                flag = 1;
            }
            if (flag)
            { 
                dp[i][0] = 0;
            }
        }

        flag = 0;

        for (int i = 0; i < n; i++)
        {
            if (obstacleGrid[0][i] == 1)
            {
                flag = 1;
            }
            if (flag)
            { 
                dp[0][i] = 0;
            }
        }

        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
            {
                if (obstacleGrid[i][j] == 1)
                    dp[i][j] = 0;
                else
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        return dp[m - 1][n - 1];
    }
};