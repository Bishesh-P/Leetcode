class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count = {}
        
        for i in range(len(nums)):
            if sorted_nums[i] not in count:
               count[sorted_nums[i]] = i
        return [count[num] for num in nums]
                