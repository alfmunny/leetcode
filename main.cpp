#include <iostream>
#include <queue>
#include <ctime>
#include <map>
#include <stack>
#include "350 Intersection of Two Arrays II\intersection_two_arrays2.h"

int main()
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::string s = "[()]{";

    time_t start = time(NULL);
    Solution x;

    std::vector<int> nums1 = { 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, };
    std::vector<int> nums2 = { 1,213,32,43,5,46,3,1,2 };

    for (int i : x.intersect(nums1, nums2))
    {
        std::cout << i << ", ";
    }

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}