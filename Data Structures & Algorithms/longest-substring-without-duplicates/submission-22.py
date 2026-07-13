class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()
        lenght = 0
        l = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(hashmap[s[r]]+1, l)
            lenght = max(lenght, r-l+1)
            hashmap[s[r]] = r
        return lenght