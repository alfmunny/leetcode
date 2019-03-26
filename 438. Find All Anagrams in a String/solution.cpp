#include <vector>
#include <iostream>

class Solution {
    public:
        std::vector<int> findAnagrams(std::string s, std::string p) {
            std::vector<int> sv(26, 0);
            std::vector<int> pv(26, 0);
            std::vector<int> res;

            if (s.size() < p.size()) return res;

            for (size_t i = 0; i < p.size(); ++i) {
                ++sv[s[i]-'a'];
                ++pv[p[i]-'a'];
            }

            if (sv == pv) res.push_back(0);

            for ( size_t i = 1; i < s.size() - p.size() + 1; ++i)
            {
                --sv[s[i-1] - 'a'];
                ++sv[s[i-1+p.size()] - 'a'];

                if (sv == pv) res.push_back(i);
            }

            return res;
        }
};

int main() 
{
    Solution x;
    std::string s = "cbaebabacd";
    std::string p = "abc";
    for ( auto c : x.findAnagrams(s, p)) std::cout << c << " ";
    return 0;
}
