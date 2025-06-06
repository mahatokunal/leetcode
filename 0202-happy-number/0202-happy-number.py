class Solution:
    def nextNumber(self, n: int) -> int:
        total = 0
        while n>0:
            d = n%10
            total += d*d
            n = n//10
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.nextNumber(n)

        while fast!=1 and fast!=slow:
            slow = self.nextNumber(slow)
            fast = self.nextNumber(self.nextNumber(fast))
        
        return fast==1