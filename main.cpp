#include <iostream>
#include <queue>
#include "300 LIS/LIS.h"

int main() 
{
    vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    LIS x;

    std::cout << x.lengthOfLIS(a);

	system("PAUSE");
    return 0;
}