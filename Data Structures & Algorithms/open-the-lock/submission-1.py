class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # let's use breath first search here
        if "0000" in deadends:
            return -1

        q = collections.deque()
        q.append(["0000", 0])
        visit = set(deadends)
        
        def childrens(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in childrens(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns+1])
        return -1