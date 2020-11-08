class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) < 2:
            return True
        
        dp = defaultdict(lambda: [0, 0, 0])
        dp[1][1] = 1
        
        for i in stones[1:]:
            for j in range(3):
                if dp[i][j] == 0:
                    continue
                for k in [-1, 0, 1]:
                    step = dp[i][j] + k
                    if i+step == stones[-1]:
                        return True
                    elif step > 0 and i + step < stones[-1]:
                        dp[i+step][k+1] = max(dp[i+step][k+1], dp[i][j]+k)
                        
        return False
