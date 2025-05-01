class Solution:
    def calculateHours(self, k, piles):
        sum = 0
        for pile in piles:
            sum+=math.ceil(pile/k)
        return sum
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while(l<r):
            mid=(l+r)//2
            n_hours=self.calculateHours(mid, piles)
            if n_hours<=h:
                r=mid
            elif n_hours>h:
                l=mid+1
        return r