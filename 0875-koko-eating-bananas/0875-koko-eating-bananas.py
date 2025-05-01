class Solution:
    def calculateHours(self, piles: List[int], speed: int) -> int:
        sum = 0
        for pile in piles:
            sum = sum + (pile+speed-1)//speed
        return sum
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l=1
        while l<r:
            mid = r + (l-r)//2
            n_hours = self.calculateHours(piles, mid)
            # print("l = ", l, " r = ", r, " n_hours = ", n_hours)
            if n_hours<=h:
                r = mid
            elif n_hours>h:
                l = mid+1
        return l
        