class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # there are 2 conditions which
        # 1. if w1 is prefix of w2 there w1 should be before of w2
        # 2. order of w1 should be less than the w2

        seq = {c : i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False

                if w1[j] != w2[j]:
                    if seq[w1[j]] > seq[w2[j]]:
                        return False
                    break
        return True