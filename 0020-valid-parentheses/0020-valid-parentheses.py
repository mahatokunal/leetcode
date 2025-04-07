class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            if ( s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                ord_diff = ord(s[i])-ord(top)
                if ord_diff!=1 and  ord_diff!=2:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

