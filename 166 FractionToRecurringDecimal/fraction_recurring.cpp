#include "fraction_recurring.h"

string Solution::fractionToDecimal(long long numerator, long long denominator) {
    if (numerator == 0) return "0";
    char map[] = "0123456789";
    string ret;
    if(numerator < 0 ^ denominator < 0) ret += "-";
    long long num = (long long)abs(numerator);
    long long denom = (long long)abs(denominator);
    
    long long integer_n = num / denom;
    long long float_n = num % denom;
    ret += to_string(integer_n);
        
    unordered_map<long long, long long> checker;
    vector<char> tmp;
    long long counter = 0;
    bool has_repeat = false;
    long long marker;
    
    if(float_n)
    {
        ret += ".";
        while(float_n)
        {
            if(checker.count(float_n) == 0)
            {
                checker[float_n] = ++counter;
                int m = float_n * 10 / denom;
                tmp.push_back(map[m]);
                float_n = float_n * 10 % denom;
            }
            else
            {
                has_repeat = true;
                marker = checker[float_n];
                break;
            }
                
        }
    }
    
    if(!has_repeat)
    {
        for(int i = 0; i < tmp.size(); i++)
            ret += tmp[i];
    }   
    else
    {
        for(int i = 0; i < tmp.size(); i++)
        {
            if(i != marker - 1)
                ret += tmp[i];
            else
            {
                ret = ret + "(" + tmp[i];
            }
        }
        ret += ")";
    }
    
    return ret;
}