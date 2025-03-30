class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        freq = Counter(nums)
        num_buckets = n+1
        buckets = [[] for _ in range(num_buckets)]
        for key, value in freq.items():
            buckets[value].append(key)
        finalList = []
        for subList in reversed(buckets):
            if subList:
                for element in  subList:
                    k-=1
                    finalList.append(element)
                if k==0:
                    break
        return finalList  