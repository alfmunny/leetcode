class Solution:
    memo = {}
    def rob(self, root):
        return self.robRec(root, False)

    def robRec(self, root, isRobbed):
        if not root:
            return 0

        if (root, isRobbed) in memo:
            return memo[(root, isRobbed)]
        
        if isRobbed:
            ans = self.robRec(root.left, False) + self.robRec(root.right, False)
        else:
            ans = max(root.val + self.robRec(root.left, True) + self.robRec(root.right, True),
                      self.robRec(root.left, False) + self.robRec(root.right, False))

        memo[(root, isRobbed)] = ans

        return ans
