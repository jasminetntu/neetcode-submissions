class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return self.helpPermute(nums, [], [], [])
    
    def helpPermute(self, nums, result, currPerm, visited):
        if len(currPerm) == len(nums):
            result.append(currPerm.copy())
        else:
            for num in nums:
                if num not in visited:
                    currPerm.append(num)
                    visited.append(num)
                    self.helpPermute(nums, result, currPerm, visited)

                    # undo
                    currPerm.pop()
                    visited.pop()

        return result
        