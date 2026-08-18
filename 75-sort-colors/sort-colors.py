class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0

        while i < len(nums):
            j = i + 1

            while j < len(nums):
                if nums[j] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

                j += 1

            i += 1