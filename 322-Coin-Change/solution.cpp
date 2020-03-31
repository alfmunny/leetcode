#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
    public:
        int coinChange(std::vector<int> coins, int amount)
        {
            std::vector<int> dp(amount+1, amount+1);
            int n = coins.size();
            dp[0] = 0;
            for (int i = 0; i < amount + 1; i++) {
                for (int j = 0; j < n; j++) {
                    if ( coins[j] <= i) {
                        dp[i] = std::min(dp[i], dp[i - coins[j]] + 1);
                    }
                }
            }
            return dp[amount] > amount ? -1 : dp[amount];
        }
};

int main()
{
    Solution x;
    std::vector<int> a{1, 2, 5};
    int amount = 23;
    int ret = x.coinChange(a, amount);
    std::cout << ret << std::endl;
    return 1;
}
