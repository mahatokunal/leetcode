class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        charSet = set()
        max_subStr=0
        n = len(s)
        for r in range(0, n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            max_subStr = max(max_subStr, r-l+1)
        return max_subStr