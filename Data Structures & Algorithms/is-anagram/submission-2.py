class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #lets use a hash map
        count_s = dict()
        for key in s:
            count_s[key] = count_s.get(key, 0) + 1
        count_t = dict()
        for key in t:
            count_t[key] = count_t.get(key, 0) + 1

        return count_s == count_t