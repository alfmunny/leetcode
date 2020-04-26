class Solution:
    def pathSum(self, root, sum):
        if not root:
            return 0

        return self.pathSum(root.left, sum) + self.pathSum(
            root.right, sum) + self.pathSumFrom(root, sum)

    def pathSumFrom(self, root, sum):

        if not root:
            return 0

        if root.val == sum:
            return 1 + self.pathSumFrom(root.left, 0) + self.pathSumFrom(
                root.right, 0)
        else:
            return self.pathSumFrom(root.left,
                                    sum - root.val) + self.pathSumFrom(
                                        root.right, sum - root.val)
