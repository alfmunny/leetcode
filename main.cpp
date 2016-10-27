#include <iostream>
#include <queue>
#include <ctime>
#include "62 Unique Paths\UniquePaths.cpp"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    time_t start = time(NULL);

    int m = 6;
    int n = 4;
    UniquePaths x;

    std::cout << x.UniquePathsTwoDim(2, 2) << std::endl;

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}