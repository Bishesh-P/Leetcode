class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minspeed = 1
        maxspeed = max(piles)
        while minspeed < maxspeed:
            mid = (minspeed + maxspeed) // 2

            if self.canEatinTime(piles,h, mid):
                maxspeed = mid
            else:
                minspeed = mid + 1

        return minspeed
    def canEatinTime(self, piles, h , speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/speed)
        return hours <= h
        