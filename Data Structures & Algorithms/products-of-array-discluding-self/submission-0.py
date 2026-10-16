class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        result = [1]*len(nums)
        
        n_p = 1
        for i in range(len(nums)):
            prefix[i] = n_p
            n_p *= nums[i]
        n_s = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = n_s
            n_s *= nums[i]
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        return result
