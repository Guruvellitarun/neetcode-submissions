class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort_strs = sorted(strs)
        # group = dict()
        # for index, value in enumerate(strs):
        #     value = sorted(value)
        #     group[value] = index
        # print(group)

        result = []
        group = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            group[sorted_s].append(s)
        for value in group.values():
            result.append(value)
        return result