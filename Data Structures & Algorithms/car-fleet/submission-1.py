class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # here we can solve it by checking the time to reach

        value = sorted(zip(position, speed))
        stack = []
        for p, s in reversed(value):
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)