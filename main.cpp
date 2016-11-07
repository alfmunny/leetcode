#include <iostream>
#include <queue>
#include <ctime>
#include "442 Find All Duplicates in an Array\solution.h"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::vector<int> n{2, 1, 2, 3, 3, 4, 5};

    time_t start = time(NULL);

    Solution x;

    for (int i : x.findDuplicates(n))
    {
        std::cout << i << ", ";
    }

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}