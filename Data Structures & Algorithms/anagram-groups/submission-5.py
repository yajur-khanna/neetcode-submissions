class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                pos = ord('a') - ord(j)
                count[pos] += 1
            word[tuple(count)].append(i)
        return list(word.values())