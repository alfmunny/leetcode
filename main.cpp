#include <iostream>
#include <queue>
#include <ctime>
#include <map>
#include <stack>
#include "338 Counting Bits\countBits.h"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::string s = "[()]{";

    time_t start = time(NULL);
    CountBits x;

    for(int i : x.countBitsVersion1(5))
        std::cout <<  i << std::endl;

    for(int i : x.countBitsVersion2(5))
        std::cout <<  i << std::endl;

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}