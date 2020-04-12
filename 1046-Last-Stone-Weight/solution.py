class Solution:
    def lastStoneWeight(self, stones):
        res = [ -s for s in stones ] 
            
        heapq.heapify(res)
        
        while len(res) > 1 :
            y = heapq.heappop(res)
            x = heapq.heappop(res)
            if y != x:
                heapq.heappush(res, y-x)
                
        return res[0]*-1 if res else 0
