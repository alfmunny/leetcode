#include "remove_element.h"

int Solutiont::removeElement(vector<int>& nums, int val)
{
    int ret = 0;
    int index = 0;
    for(int i = 0; i < nums.size(); ++i)
    {
        if(nums[i] != val) 
        {
            ++ret;
            nums[index++] = nums[i];
        }
    }
    return ret;
}
