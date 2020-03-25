class Solution:
    def canReach(self, arr, start):
        if start >= len(arr) or start < 0:
            return False

        if arr[start] == 0:
            return True

        if arr[start] == -1:
            return False

        step = arr[start]
        arr[start] = -1

        if self.canReach(arr, start - step) or self.canReach(arr, start + step):
            return True
        else:
            arr[start] = step
            return False
