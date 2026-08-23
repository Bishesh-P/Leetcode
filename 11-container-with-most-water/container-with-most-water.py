class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        n = len(height)
        right = n-1

        while left<right:
            width = right - left
            h = min(height[left], height[right])
            ans = max(ans, h * width)
            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        return ans 
        
        
        