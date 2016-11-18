#include "countBits.h"


std::vector<int> CountBits::countBitsVersion1(int num) {
        std::vector<int> dp(num+1, 0);
        for(int i = 1; i < num + 1; i++)
        {
            dp[i] = dp[i&(i - 1)] + 1; 
        }
        return dp;
}

std::vector<int> CountBits::countBitsVersion2(int num) {
        std::vector<int> dp(num+1, 0);
        for(int i = 1; i < num + 1; i++)
        {
            dp[i] = i % 2 + dp[i / 2];
        }
        return dp;
}