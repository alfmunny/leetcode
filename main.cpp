#include <iostream>
#include <queue>
#include <ctime>
#include "63 Unique Paths II\UniquePathsII.cpp"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    vector<vector<int>> a = {
        vector<int>{0, 1, 0},
        vector<int>{0, 0, 0},
        vector<int>{0, 0, 0},
    };

    time_t start = time(NULL);

    int m = 6;
    int n = 4;
    UniquePathsII x;

    std::cout << x.UniquePathsWithObstacles(a) << std::endl;

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}