#include <iostream>
#include <queue>
#include <ctime>
#include <map>
#include <stack>
#include "204 Count Primes\count_primes.cpp"

int main() 
{
    //vector<int> a = { 1, 2, 3, 10, 100, 77, 1,2,34,45,654,234,12,312,45,43};
    std::string s = "[()]{";

    time_t start = time(NULL);
    Solution x;

    std::cout << x.countPrimes(24999);

    time_t end = time(NULL);

    //std::cout << double(end - start) / CLOCKS_PER_SEC << std::endl;

	system("PAUSE");
    return 0;
}