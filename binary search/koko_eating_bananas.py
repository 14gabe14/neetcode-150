import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_speed = int(math.ceil(sum(piles) / h))
        max_speed = max(piles)

        best_speed = math.inf

        while(min_speed < max_speed):
            m = (min_speed + max_speed) // 2

            h_m = sum(int(math.ceil(pile/m)) for pile in piles)

            if h_m > h:
                min_speed = m + 1
            else:
                max_speed = m
                
        return min_speed
