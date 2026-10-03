class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # decreasing stack of indices
        
        for i in range(2 * n):
            idx = i % n
            # Pop all indices whose next greater element is nums[idx]
            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]
            
            # Only push during the first pass
            if i < n:
                stack.append(idx)
        
        return result
        