class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        f = len(flowerbed)
        count = 0

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, f + 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False