class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        instability_score = 0
        n = len(nums)
        for i in range(n):
            instability_score = max(nums[0:i+1]) - min(nums[i:n])

            if instability_score <= k:
                return i
                
        return -1


        