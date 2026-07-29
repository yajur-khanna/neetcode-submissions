class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for i in nums:
            j = i
            longest = 1
            if j-1 not in hashset:
                while j+1 in hashset:
                    longest += 1
                    j +=1
            res = max(longest, res)
        return res