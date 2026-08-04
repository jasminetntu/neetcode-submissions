class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if target in nums else -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            print(nums[l], nums[mid], nums[r])

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]: # right is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # left is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # if nums[mid] == target:
            #     return mid
            # elif nums[mid] > target:
            #     r = mid - 1
            # else:
            #     l = mid + 1
        
        if nums[l] == target:
            return l

        return -1
        