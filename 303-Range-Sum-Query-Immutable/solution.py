class NumArray:
    def __init__(self, nums: List[int]):
        self.dp = list(nums)
        self.dp.insert(0, 0)
        for i in range(1, len(nums)):
            self.dp[i+1] += self.dp[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]
