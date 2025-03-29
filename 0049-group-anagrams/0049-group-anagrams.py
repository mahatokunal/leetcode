class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in sorted_dict:
                sorted_dict[sorted_str].append(s)
            else:
                sorted_dict[sorted_str]=[s]
        return list(sorted_dict.values())