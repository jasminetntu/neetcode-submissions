class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # len(result) will always be 2^n

        result = [[]]
        
        for i in range(len(nums)):
            temp = result.copy()
            for j in range(len(temp)):
                new = temp[j].copy()
                new.append(nums[i])

                result.append(new)

        return result