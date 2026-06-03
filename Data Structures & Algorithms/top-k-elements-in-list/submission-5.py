class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for keys, values in count.items():
            freq[values].append(keys)
        for n in range(len(freq)-1, 0, -1):
            for j in freq[n]:
                res.append(j)
                if len(res) == k:
                    return res