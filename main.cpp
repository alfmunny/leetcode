#include <iostream>
#include <queue>
#include "119 Pascal'sTriangleII\PascalsTriangleII.h"

int main() 
{
    for (int i : pascalTriangleGetRow(6))
    {
        std::cout << i << " ";
    }
	system("PAUSE");
    return 0;
}