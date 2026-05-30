class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        word_1 = {}
        word_2 = {}

        for i in s:
            word_1[i] = word_1.get(i, 0) + 1

        for j in t:
            word_2[j] = word_2.get(j, 0) + 1

        if word_1 == word_2:
            return True

        return False