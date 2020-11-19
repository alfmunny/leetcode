class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(row[0], index, 0) for index, row in enumerate(matrix)]
        heapify(heap)
        while k > 0:
            ret, i, j = heapq.heappop(heap) 
            if j+1 < n:
                heappush(heap, (matrix[i][j+1], i, j+1))    
            k -= 1
        return ret
