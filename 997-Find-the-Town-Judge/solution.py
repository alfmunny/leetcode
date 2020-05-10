class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        people = [0] * (N)
        h = defaultdict(int)
        
        for t in trust:
            people[t[1]-1] += 1
            h[t[0]-1] = 1
        
        for i in range(N):
            if people[i] >= N - 1 and h[i] == 0:
                return i+1
            
        return -1
