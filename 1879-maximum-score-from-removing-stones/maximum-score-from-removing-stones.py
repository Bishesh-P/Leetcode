class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a,b,c = sorted([a,b,c])
        return min((a+b+c) // 2, a+b)



        