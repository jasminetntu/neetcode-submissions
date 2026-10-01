class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix & suffix arrays
        # product at each idx is prefix * suffix
        # iterate through nums -> multiply each index with its prefix
        # iterate through nums again -> multiply each index with its suffix
        # whatever's remaining is the output

        ans = []

        prefix = 1
        for i in range(len(nums)):
            ans.append(prefix)
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans