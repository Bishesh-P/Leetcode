class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        mincost = [0] * (n+1)
        for i in range(2, n+1):
            mincost[i] = min((cost[i-2]+ mincost[i-2]), (cost[i-1]+mincost[i-1]))
        
        return mincost[n]
        

