#include <vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        if(n == 0 || n == 1) return 0;
        vector<int> dp(n, 1);
        dp[0] = 0;
        dp[1] = 0;
        int count = n - 2;
        for(int i = 2; i * i < n; i++)
        {
            if(dp[i] == 1)
            {
                for(int j = i; j * i < n; j++)
                {
                    if(dp[j*i] == 1)
                    {
                        dp[j * i] = 0;
                        count --;    
                    }
                }
            }
        }
        return count;
    }
};
