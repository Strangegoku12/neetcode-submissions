from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculate(piles, speed):
            totalhrs = 0

            for i in range(len(piles)):
                totalhrs += ceil(piles[i] / speed)

            return totalhrs

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            totalhrs = calculate(piles, mid)

            if totalhrs <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low