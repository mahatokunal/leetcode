class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0]*26
        freq_t = [0]*26
        i = 0
        j = 0
        while (i<len(s) or j<len(t)):
            if (i<len(s)):
                # print("ord(s[i] = ", ord(s[i]))
                freq_s[ord(s[i]) - ord('a')]+=1
            if (i<len(t)):
                # print("ord(t[j] = ", ord(t[j]))
                freq_t[ord(t[j]) - ord('a')]+=1
            i+=1
            j+=1
        for i in range(0, 26):
            # print(freq_s[i], freq_t[i])
            if(freq_s[i]!=freq_t[i]):
                return False
        return True 
        