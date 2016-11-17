#include <iostream>
#include <queue>
#include <ctime>
#include <map>
#include <stack>
#include "290 Word Pattern\word_pattern.h"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::string s = "[()]{";

    time_t start = time(NULL);
    WordPattern x;
    std::string pattern = "abba";
    std::string str = "boy girl girl boy";

    std::cout << x.wordPattern(pattern, str) << std::endl;

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}