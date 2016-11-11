#include "solution.h"

using namespace std;

int Solution::hIndex(vector<int>& citations) {
        int n = citations.size();
        int res = 0;
        if (n == 0)
            return 0;
        
        int total = 0;
        vector<int> h_index = vector<int>(n+1, 0);
        
        for (int i : citations)
        {
            if (i >= n)
            {
                h_index[n]++;
            }
            else
            {
                h_index[i]++;
            }
        }
        
        for (int i = n; i >=0; i--)
        {
            if (total < i)
            {
                total += h_index[i];
                res = i;
            }
            else
            {
                break;
            }

        }
        return res;
};