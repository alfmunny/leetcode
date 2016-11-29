#include <iostream>
#include <queue>
#include <ctime>
#include <map>
#include <stack>
#include "315 CountSmaller\countSmaller.h"

int main()
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::string s = "[()]{";

    time_t start = time(NULL);
    vector<int> nums = { 5, 2, 6, 1 };
    Solution x;

    // -1 -2147483648

    for (int v : x.countSmaller(nums))
    {
       std::cout << v << ", ";
    }

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}