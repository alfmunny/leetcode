#include <iostream>
#include <queue>
#include "121 BestTimeToBuyAndSellStock\BestTimeToBuyAndSellStock.h"

int main() 
{
    vector<int> a = { 1, 2, 3, 10, 100, 77,1,2,34,45,654,234,12,312,45,43};
    BestTimeToBuyAndSellStock x;

    std::cout << x.maxProfit(a);

	system("PAUSE");
    return 0;
}