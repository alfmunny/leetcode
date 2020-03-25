class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        histograms = [[0] * n for i in range(m)]

        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    histograms[i][j] = histograms[i - 1][j] + 1 if i > 0 else 1

        for histogram in histograms:
            res = max(res, self.largestRectangleHistogram(histogram))

        return res

    def largestRectangleHistogram(self, histogram):

        if not histogram:
            return 0

        stack = []
        res = 0
        index = 0
        n = len(histogram)

        while index < n:
            if not stack or histogram[index] >= histogram[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                res = max(
                    res, histogram[stack.pop()] *
                    ((index - stack[-1] - 1) if stack else index))

        while stack:
            height = histogram[stack.pop()]
            res = max(res, height * ((n - stack[-1] - 1) if stack else n))

        return res

maxtrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(Solution().maximalRectangle(maxtrix))
