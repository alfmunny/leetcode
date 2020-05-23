class Solution:
    def intervalListIntersection(self, A, B):
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            left = max(A[i][0], B[j][0])
            right = min(A[i][1], B[j][1])
            if left <= right:
                ans.append([left, right])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
