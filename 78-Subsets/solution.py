class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

print(Solution().subsets([1, 2, 3]))

class Solution:

    def subsets(self, nums):
        res = [[]]
        for i in sorted(nums):
            res += [item+[i] for item in res]

        return res

print(Solution().subsets([1, 2, 3]))

class Solution(object):

    def subsets(self, nums):
        output = []
        for k in range(0, len(nums)+1):
            temp = []
            self.backtrack(0, k, nums, temp, output)

        return output

    def backtrack(self, begin, length, nums, temp, output):

        if length == len(temp):
            output.append(temp[:])

        for i in range(begin, len(nums)):
            temp.append(nums[i])
            self.backtrack(i+1, length, nums, temp, output)
            temp.pop()


print(Solution().subsets([1, 2, 3]))

class Solution():
  def subsets(self, nums):
    n = len(nums)
    output = []
    for i in range(2**n, 2**(n+1)):
      bitmask = bin(i)[3:]
      output.append([nums[i] for i in range(n) if bitmask[i] == '1' ])

    return output
