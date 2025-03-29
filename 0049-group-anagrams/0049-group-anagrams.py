from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            hashing = [0] * 26
            for char in s:
                hashing[ord(char) - ord('a')] += 1
            my_dict[tuple(hashing)].append(s)
        return list(my_dict.values())