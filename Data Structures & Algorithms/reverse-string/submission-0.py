class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left = 0
        # right = len(s)-1
        # while left < right:
        #     first_element = s.pop(left)
        #     last_element = s.pop(right)
        #     s.insert(right, first_element)
        #     s.insert(left, last_element)
        #     left += 1
        #     right -= 1
        s.reverse()
