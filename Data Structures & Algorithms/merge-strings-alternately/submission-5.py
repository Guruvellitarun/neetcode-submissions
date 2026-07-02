class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        res = ""
        while r < len(word2) and l < len(word1):
            res += word1[l]
            res += word2[r]
            l += 1
            r += 1
            # if r >= len(word2) and l < len(word1):
            #     res += word1[l:]
            # elif l >= len(word1) and r < len(word2):
            #     res += word2[r:]
        res += word1[l:]
        res += word2[r:]
        return res