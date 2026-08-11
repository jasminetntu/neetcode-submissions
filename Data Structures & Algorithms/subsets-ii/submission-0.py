class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.findSubset(sorted(nums), [], [], 0)
    
    def findSubset(self, nums, result, currSubset, i):
        if currSubset not in result:
            result.append(currSubset.copy())
        if i >= len(nums):
            return result
        
        # take curr
        currSubset.append(nums[i])
        self.findSubset(nums, result, currSubset, i + 1)
        currSubset.pop()

        # skip dup
        while i < len(nums) - 1 and nums[i + 1] == nums[i]:
            i += 1

        # skip curr
        self.findSubset(nums, result, currSubset, i + 1)

        return result