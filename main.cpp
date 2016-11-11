#include <iostream>
#include <queue>
#include <ctime>
#include "274 H-Index\solution.h"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::vector<int> n{2, 1, 2, 3, 3, 4, 5};

    time_t start = time(NULL);

    Solution x;
    std::cout << x.hIndex(n) << ", " << INT_MIN << ", " << INT_MAX;

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}