class Solution:
    def letterCombination(self, digits):
          m = {
              2: "abc",
              3: "def",
              4: "ghi",
              5: "jkl",
              6: "mno",
              7: "pqrs",
              8: "tuv",
              9: "wxyz"
          }

        ans = [""]

        for d in digits:
            ans = [ ans[i] + c for c in m[int(d)] for i in range(len(ans))]

        return ans
