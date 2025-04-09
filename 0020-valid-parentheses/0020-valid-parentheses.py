class Solution:
    def isValid(self, s: str) -> bool:
        b_map = {')':'(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in b_map:
                if not stack:
                    return False
                else:
                    top=stack.pop()
                    if b_map[ch]!=top:
                        return False
            else:
                stack.append(ch)
        if stack:
            return False
        return True

