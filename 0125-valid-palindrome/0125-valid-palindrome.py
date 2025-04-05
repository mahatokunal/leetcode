class Solution:

    def getAscii(self, ch):
        if ord(ch)>= 65 and ord(ch)<=90:
            return ord(ch) + 32
        elif ord(ch)>=97 and ord(ch)<=122:
            return ord(ch)
        elif ord(ch)>=48 and ord(ch)<=57:
            return ord(ch)
        else:
            return -1

    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while(l<r):
            l_a = self.getAscii(s[l])
            r_a = self.getAscii(s[r])
            print(s[l], s[r], l_a, r_a)
            if l_a == -1 and r_a == -1:
                l+=1
                r-=1
                continue
            elif l_a==-1:
                l+=1
                continue
            elif r_a==-1:
                r-=1
                continue

            if l_a!=r_a:
                return False
            else:
                l+=1
                r-=1
        
        return True