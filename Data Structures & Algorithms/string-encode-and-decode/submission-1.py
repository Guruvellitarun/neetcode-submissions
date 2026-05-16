class Solution:
    value = ['A','a','B','b','C','c','D','d','E','e','f','F','G','g','H','h','I','i','J','j','K','k','']
    def encode(self, strs: List[str]) -> str:
        encode = ''
        for ch in strs:
            encode += ch + '1#a'
        return encode

    def decode(self, s: str) -> List[str]:
        original = s.split('1#a')
        return original[:-1]