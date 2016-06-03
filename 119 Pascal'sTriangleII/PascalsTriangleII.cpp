#include "PascalsTriangleII.h"
#include <iostream>

vector<int> pascalTriangleGetRow(int rowIndex)
{
    vector<int> dp(rowIndex + 1, 1);
    dp[0] = 1;

    for (size_t i = 1; i < dp.size() - 1; i++)
    {
        for (size_t j = i; j > 0; j--)
        {
            dp[j] = dp[j] + dp[j - 1];
        }
    }
    return dp;
}