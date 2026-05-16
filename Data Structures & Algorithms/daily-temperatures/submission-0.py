class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][1]:
                indexT, tempT = stack.pop()
                res[indexT] = index - indexT
            stack.append([index, value])
        return res

        # for index, temp in enumerate(temperatures):
        #     while stack and temp > stack[-1][0]:
        #         tempT, indexT = stack.pop()
        #         res[indexT] = index - indexT
        #     stack.append([temp, index])
        # return res