#include <vector>
#include <iostream>
#include <map>

using namespace std;

class Solution {
    public:
        int leastInterval(vector<char>& tasks, int n) {
            vector<int> counter(26, 0);
            int tasks_n = tasks.size();
            int max_val = 0;
            int max_count = 0;

            for (char c : tasks)
            {
                counter[c - 'A']++;
            }

            max_val = *max_element(counter.begin(), counter.end());

            for (int x : counter) 
            {
                if (x == max_val) max_count++;
            }   

            int idle_slots = (max_val - 1) * (n - (max_count - 1)) - (tasks_n - max_count * max_val);

            return idle_slots > 0 ? idle_slots + tasks_n : tasks_n;
        }
};

int main()
{
    vector<char> input= { 'A', 'A', 'A', 'B', 'B', 'B'};
    int n = 50;
    Solution x;
    cout << x.leastInterval(input, n);
    return 0;
}
