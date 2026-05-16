class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        count = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            count[sorted_s].append(s)
        for value in count.values():
            result.append(value)
        return result