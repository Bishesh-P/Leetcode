class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = count = 0
        for char in s:
            if char == 'L' : count +=1
            if char == 'R' : count -=1
            if count == 0: ans +=1
        return ans
        