class Solution:
    def largestRectangleArea(self, heights):

        if not heights:
            return 0

        n = len(heights)
        res = 0

        left = [ i for i in range(n) ]
        right = [ i for i in range(n) ]

        # caculate for the left edge
        for i in range(n):
            p = i
            while p >= 0:
                if heights[p] < heights[i]:
                    break
                p -= 1
            left[i] = p

        # caculate for the right edge
        for i in range(n):
            p = i
            while p < n:
                if heights[p] < heights[i]:
                    break
                p += 1
            right[i] = p

        for i in range(n):
            res = max(res, heights[i] * (right[i] - left[i] - 1))

        return res

print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))

class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        res = 0
        n = len(heights)
        left = [1] * n
        right = [1] * n

        # caculate left[]
        for i in range(n):
            p = i - 1
            while p >= 0:
                if heights[p] >= heights[i]:
                    left[i] += left[p]
                    # jump backward
                    p -= left[p]
                else:
                    break

        # caculate right[]
        for i in range(n - 1, -1, -1):
            p = i + 1
            while p < n:
                if heights[p] >= heights[i]:
                    right[i] += right[p]
                    # jump forward
                    p += right[p]
                else:
                    break

        for i in range(n):
            res = max(res, heights[i] * (left[i] + right[i] - 1))

        return res

print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))

class Solution:
    def largestRectangleArea(self, heights):

        stack = []
        n = len(heights)
        res = 0
        index = 0

        while index < n:

            if not stack or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                top = stack.pop()
                area = (heights[top] *
                        ((index - stack[-1] - 1) if stack else index))

                res = max(res, area)

        while stack:
            h = stack.pop()
            res = max(
                res,
                heights[h] * ((n - stack[-1] - 1) if stack else n))

        return res


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
