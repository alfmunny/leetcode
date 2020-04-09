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
                r
