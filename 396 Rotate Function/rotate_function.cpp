#include <string>
#include <stack>
#include <map>

class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        if(A.size() == 0) return 0;
        int sum = 0;
        int f = 0;
        for(int i = 0; i < A.size(); ++i) 
        {
            f += i*A[i];
            sum += A[i];
        }

        int ret = f;

        for(int i = 1; i < A.size(); ++i)
        {
            f = f + sum - A.size()*A[A.size() - 1 - (i - 1)];
            ret = max(f, ret);
        }
        return ret;
    }
};
