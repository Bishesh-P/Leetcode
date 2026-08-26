class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 1. Reverse the entire array
        reverse(0, n - 1)

        # 2. Reverse the first k elements
        reverse(0, k - 1)

        # 3. Reverse the remaining elements
        reverse(k, n - 1)
        