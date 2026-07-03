class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1 = list(s1)
        s1.sort()
        l = 0
        for r in range(len(s1)-1, len(s2)):
            val = list(s2[l:r+1])
            val.sort()
            if val == s1:
                return True
            l += 1
        return False