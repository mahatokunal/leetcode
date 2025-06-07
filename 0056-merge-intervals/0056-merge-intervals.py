class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        merged = []

        for start, end in intervals:
            if not merged or start>merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        return merged
      
# [1,3],[2,6],[8,10],[15,18]
# merged - [1,6], [8,10], [15,18]

# [1,4],[4,5]
# merged [1,5]