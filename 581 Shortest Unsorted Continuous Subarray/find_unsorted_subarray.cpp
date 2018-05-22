#include <iostream>
#include <vector>
using namespace std;

class UnsortedSubarray {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int max = nums[0];
        int left = 0;
        int right = 0;
        bool flag = false;

        for (size_t i = 0; i < nums.size(); i++)
        {
            if(nums[i] >= max) 
            {
                max = nums[i];
            }
            else if (nums[i] < max) {
                if (!flag) left = i;
                right = i;
                int j = i - 1;
                int localIndex = i;
                while( j >= 0 ) {
                    if (nums[j] > nums[i] )
                    {
                        localIndex = j;
                        j--;
                    }
                    else break;
                }
                if ( localIndex < left) left = localIndex;
                flag = true;
            }
            
        }
        cout << "left" << left << endl;
        cout << "right" << right << endl;
        if (flag) return right - left + 1;
        else return 0;
    }
};


int main() {
    UnsortedSubarray x;
    vector<int> nums{2, 6, 4, 8, 10, 9, 15};
    vector<int> num1{2, 3, 3, 2, 4};
    vector<int> num2{1, 3, 5, 4, 2};
    vector<int> num3{1, 3, 2, 2, 2};
    vector<int> num4{-1, -1, -1, -1, -1};

    cout << x.findUnsortedSubarray(num4) << endl;

    return 0;
}
