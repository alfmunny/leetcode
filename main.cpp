#include <iostream>
#include <queue>
#include <ctime>
#include <map>
#include <stack>
#include "78 Subsets\subsets.h"

int main()
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::string s = "[()]{";

    time_t start = time(NULL);
    vector<int> nums = { 1, 2, 3 };
    Solution x;

    // -1 -2147483648

    for (vector<int> vv : x.subsets(nums))
    {
        for (int v : vv)
            std::cout << v << ", ";

        std::cout << std::endl;
    }



    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}