class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        leftHeight = self.leftMaxHeight(height)
        rightHeight = self.rightMaxHeight(height)

        for i in range(len(height)):
            max_bar = min(leftHeight[i], rightHeight[i])
            if max_bar > height[i]:
                ans += max_bar - height[i]
        return ans
        
    def leftMaxHeight(self, height):
        ans = [0] * len(height)
        max_left = 0
        for i in range(len(height)):
            ans[i] = max_left
            max_left = max(height[i], max_left)
        return ans
    
    def rightMaxHeight(self, height):
        ans = [0] * len(height)
        max_right = 0
        for i in range(len(height)-1, -1, -1):
            ans[i] = max_right
            max_right = max(height[i], max_right)
        return ans
