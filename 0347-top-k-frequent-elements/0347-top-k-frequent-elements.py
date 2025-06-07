class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        min_heap = []
        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)

        ans=[]
        for count, num in min_heap:
            ans.append(num)
        
        return ans

# freq: {1:3, 2:2, 3:1}