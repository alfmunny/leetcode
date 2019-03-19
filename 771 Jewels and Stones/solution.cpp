#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using std::string;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int a[200] = {0};
        int ret = 0;
        for ( size_t i = 0; i < J.length(); ++i )
            a[J[i]] = 1;
        for ( size_t i = 0; i < S.length(); ++i )
            if (a[S[i]]) ++ret;
        return ret;
    }
};


int main() 
{
    Solution x;
    std::string j = "aAs";
    std::string s = "aAAAAbbbbssscc";

    std::cout << x.numJewelsInStones(j, s) << std::endl;
    return 0;
}
