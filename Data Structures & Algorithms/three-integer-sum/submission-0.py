class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        

        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and v == nums[i-1]:
                continue

            f, l = i+1, len(nums)-1

            while f < l:
                count = nums[i] + nums[f] + nums[l]
                if count > 0:
                    l -= 1
                elif count < 0:
                    f += 1
                else:
                    res.append([nums[i], nums[f], nums[l]])
                    f += 1
                    l -= 1
                    while nums[f] == nums[f-1] and f < l:
                        f += 1
        return res 