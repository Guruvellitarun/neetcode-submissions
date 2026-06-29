class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1st will sort the array nums.
        nums.sort()

        # 2nd we need to find the triplet
        res = [] # This is where we are going to store the result
        for t_index, value in enumerate(nums):
            if t_index > 0 and nums[t_index] == nums[t_index - 1]:
                continue
            l, r = t_index + 1, len(nums)-1
            while l < r:
                total_sum = nums[t_index] + nums[l] + nums[r]
                if total_sum < 0:
                    l += 1
                elif total_sum > 0:
                    r -= 1
                else:
                    res.append([nums[t_index], nums[l], nums[r]])
                    l, r = l+1, r-1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res