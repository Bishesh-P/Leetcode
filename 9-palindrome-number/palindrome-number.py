class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        rev = 0
        temp = x
        while x > 0:
            digit = x % 10
            rev = rev*10 + digit
            x = x // 10
        if temp == rev :
            return True
        else:
            return False


p1 = Solution()
p1.isPalindrome(121)
        