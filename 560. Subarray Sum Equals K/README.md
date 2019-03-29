# "560. Subarray Sum Equals K"

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2


Two solutions:

## Solution 1 

Calculate every sum between two numbers, remember them in an array.

nums = 1, 2, 3

map = 

1, 3, 6 
0, 2, 5
0, 0, 3

```c++
for i in nums.size()
    for j in i
        map[i][j] = map[i-1][j] - map[i-1][i-1]
```

No need to keep the whole map.

After go through a row, you can overwrite the row with next row. 

##  Solution 2

Use hash map two remember the frequncy of every sum.
If hash[sum - k] exists, it means the nums in between can be added upto k, then result + 1

nums = 1, 2, 3
k = 3
hash = {0:1} (when sum - k = 0, result + 1)

| hash    | {0:1, 1:1} | {0:1, 1:1, 3:1}   | {0:1, 1:1, 3:1, 6:1} |
|---------|------------|-------------------|----------------------|
| sum     | 1          | 3                 | 6                    |
| sum - k | -2         | 0(exists in hash) | 3(exists in hash)    |
| result  | 0          | 1                 | 2                    |

