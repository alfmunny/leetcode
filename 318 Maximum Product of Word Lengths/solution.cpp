#include "solution.h"
using namespace std;

 int Solution::maxProduct(std::vector<std::string>& words) {
    int length = 0;
    int newLength;
    for(size_t i = 0; i < words.size() - 1; i ++)
    {
        for(int j = i+1; j < words.size(); j++)
        {
            bool hasSameLetter = false;
            for (char & c : words[i])
            {
                for( char & d: words[j])
                    if ( c == d )
                        hasSameLetter = true;                            
                        break;
                if ( hasSameLetter )
                    break;
            }

            if ( ! hasSameLetter )
            {
                newLength = words[i].length() * words[j].length();
                std::cout << newLength << std::endl;
                length = std::max(length, newLength);
            }
        }   
        return length;
    }
 };