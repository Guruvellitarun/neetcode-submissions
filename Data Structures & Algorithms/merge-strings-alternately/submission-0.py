class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if not word1 or not word2:
            return word1+word2

        def merge(word1, word2, length):
            result = ''
            for i in range(length):
                result += word1[i] + word2[i]
            return result
        
        if len(word1) > len(word2):
            length = min(len(word1), len(word2))
            value = merge(word1, word2, length)
            return value + word1[length:]
        elif len(word2) > len(word1):
            length = min(len(word1), len(word2))
            value = merge(word1, word2, length)
            return value + word2[length:]
        elif len(word1) == len(word2):
            length = len(word1)
            return merge(word1, word2, length)
