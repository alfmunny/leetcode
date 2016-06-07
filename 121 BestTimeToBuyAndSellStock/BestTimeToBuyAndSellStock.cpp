#include "BestTimeToBuyAndSellStock.h"
#include <math.h>
#include <algorithm>

int BestTimeToBuyAndSellStock::maxProfit(vector<int>& prices)
{
    int ret = 0;
    int minPrice = INT_MAX;

    for ( int x : prices)
    {
        minPrice = min(minPrice, x);
        ret = max((x - minPrice), ret);
    }
    return ret;
}