class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currsum = 0
        maxsum = float('-inf')
        for i in range(n):
            currsum = currsum+nums[i]
            maxsum = max(maxsum,currsum)
            if currsum<0:
                currsum = 0
        return maxsum

            
        
        