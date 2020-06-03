class Solution:
    def twoCitySchedCost(self, costs):
        sortedCosts = sorted(costs, key=lambda cost: cost[0] - cost[1])

        minCost = 0
        N = len(costs)

        for i in range(N//2):
            minCost += sortedCosts[i][0]
            minCost += sortedCosts[N//2+i][1]

        return minCost
