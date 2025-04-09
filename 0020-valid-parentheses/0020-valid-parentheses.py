class Solution:
    def isValid(self, s: str) -> bool:
        b_map = {')':'(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in b_map:
                if not stack:
                    # print('a')
                    return False
                else:
                    top=stack.pop()
                    if b_map[ch]!=top:
                        # print('b')
                        # print('ch = ', ch , 'b_map[ch] = ', b_map[ch], "top = ", top)
                        return False
            else:
                # print('c')
                stack.append(ch)
        if stack:
            return False
        return True

