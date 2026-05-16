class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = dict()
        for s in range(len(s1)):
            count1[s1[s]] = count1.get(s1[s], 0) + 1

        need = len(count1)

        for i in range(len(s2)):
            count2, res = dict(), 0
            for j in range(i, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1
                if count2[s2[j]] > count1.get(s2[j], 0):
                    break
                if count2[s2[j]] == count1[s2[j]]:
                    res += 1
                if need == res:
                    return True
        return False