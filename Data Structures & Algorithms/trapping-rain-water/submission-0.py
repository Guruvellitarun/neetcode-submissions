class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxleft, maxright = height[l], height[r]
        total_water = 0

        while l < r:
            if maxleft <= maxright:
                l += 1
                maxleft = max(height[l], maxleft)
                total_water += maxleft - height[l]
            else:
                r -= 1
                maxright = max(height[r], maxright)
                total_water += maxright - height[r]
        return total_water