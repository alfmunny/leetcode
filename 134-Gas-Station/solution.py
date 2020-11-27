class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = gap = left = 0

        for i in range(len(gas)):
            left += gas[i] - cost[i]
            if left < 0:
                start = i+1
                gap += left
                left = 0
                
        return start if left+gap >= 0 else -1
