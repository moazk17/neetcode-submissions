class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for i in range(len(nums)+1)]

        for n in nums:
            freq[n] +=1
        for n, c in freq.items():
            buckets[c].append(n)
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result

        
        