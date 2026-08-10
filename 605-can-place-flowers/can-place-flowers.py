class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        if n==0:
            return True
        for i in range(length):
            if(flowerbed[i]== 0):
                left_khali = i == 0 or flowerbed[i-1] == 0
                right_khali = i == length-1 or flowerbed[i+1] == 0
            
                if left_khali and right_khali:
                    flowerbed[i] = 1
                    n -=1

                    if n == 0:
                        return True

        return False
        