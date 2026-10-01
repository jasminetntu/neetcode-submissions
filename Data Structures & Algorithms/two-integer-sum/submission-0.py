class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # keep track of nums & indices we've seen so far
        # iterate through nums
        # check if target - curr is in seen
        # if yes, return 2 indices
        # if no, add to seen & continue
        
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]], i]
            
            seen[nums[i]] = i
        
        return [-1,-1] # never reached b/c always 1 valid pair