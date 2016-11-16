#include <vector>

class RotateArray{
public:
    void rotate(std::vector<int>& nums, int k) {
        int n = nums.size();
        if(nums.empty()||!(k%n))
            return;
        k %= n;    
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }
    
    void reverse(std::vector<int>& nums, int start, int end)
    {
        while(start < end)
        {
            std::swap(nums[start], nums[end]);
            start++;
            end--;
        }
    }
};