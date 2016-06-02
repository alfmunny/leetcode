#include <iostream>
#include <queue>
#include "16ThreeSUMClosest\ThreeSumClosest.h"

int main() 
{
	vector<int> a = {-1, 2, 1, -4, 8, -100, 7};

    int res = threeSumClosest(a, 1);

    vector<int> b = quickSort(a, 0, a.size() - 1);

    for (int i : b)
    {
        std::cout << i << std::endl;
    }

	system("PAUSE");
	return 0;
}

