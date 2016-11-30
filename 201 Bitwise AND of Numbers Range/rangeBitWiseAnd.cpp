#include "rangeBitWiseAnd.h"

int Solution::rangeBitWiseAnd(int m, int n)
{
    return (n > m) ? rangeBitWiseAnd(m / 2, n / 2) : m;
}
