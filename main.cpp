#include <iostream>
#include <queue>
#include <ctime>
#include "318 Maximum Product of Word Lengths\solution.h"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::vector<std::string> a = std::vector<std::string>{"abcw", "baz", "foo", "bar", "xtfn", "abcdef"};

    time_t start = time(NULL);

    Solution x;

    std::cout << x.maxProduct(a) << std::endl;

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}