class Solution:
    def getDigitsArray(self, num:int):
        return [int(d) for d in str(abs(num)) if d.isdigit()]

    def isHappy(self, n: int) -> bool:
        hashSet = set()
        new_num=n
        while(True):
            hashSet.add(new_num)
            digits = self.getDigitsArray(new_num)
            if len(digits)==1 and digits[0]==1:
                return True
            else:
                new_num = 0
                for digit in digits:
                    new_num += (digit*digit)
                if new_num in hashSet:
                    return False