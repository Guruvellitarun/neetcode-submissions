class Solution:
    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for values in strs:
            final_str += f"{len(values)}#{values}"
        return final_str

    def decode(self, s: str) -> List[str]:
        i = 0
        result = list()
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length

        return result
        