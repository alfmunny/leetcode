# 39 Combination Sum

nums = [2, 3, 6, 7], target = 7

return

[ 
    [2, 2, 3],
    [7]
]


Notes:

1. backtrace recursively


2. push and pop in every loop (It's like saying: try this number and pop out it to try the next one)

3. maintain a result list and a temporary list for the loop

    backtrace(resultList, tempList, nums, target, start)
