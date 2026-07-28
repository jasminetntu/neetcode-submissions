class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)

        # find the 2 halves
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] <= nums[right]: # right half = does not contain min
                right = mid
            else: # right half = contains min
                left = mid + 1

        return nums[left]

