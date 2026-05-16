class Solution:
    def simplifyPath(self, path: str) -> str:
        values = path.split('/')
        stack = []
        for value in values:
            if value == '' or value == '.':
                continue
            elif value == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(value)
        return "/" + '/'.join(stack)