class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = {}

        for i in range(len(nums)):
            idx[nums[i]] = i

        if target in idx:
            return idx[target]

        for i in range(len(nums)):
            if nums[i] > target:
                return i

        return len(nums)