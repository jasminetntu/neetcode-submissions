class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # unique indices where sum = 0
        # can have 0 or multiple solutions
        # only keep unique combos of values; order doesn't matter

        # general case
        # sort the array asc
        # keep track of curr sum
        # set curr sum to be the curr value -> curr sum will start at every index
        # ptr at beg & end
        # while ptrs dont overlap
        #   if any of the ptrs = the index of the curr sum, inc/dec ptr
        #   add both ptrs to curr sum
        #   if sum = 0, add triplet to result
        #   elif sum < 0, inc left
        #   elif sum > 0, dec right
        

        # try 1 - brute force
        sorted_nums = sorted(nums)
        result = []

        # for i in range(len(sorted_nums)):
        #     j = i + 1
        #     k = len(sorted_nums) - 1

        #     while j < k:
        #         if j == i:
        #             j += 1
        #         elif k == i:
        #             k -= 1
        #         else:
        #             curr_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
        #             curr_triplet = sorted([sorted_nums[i], sorted_nums[j], sorted_nums[k]])

        #             if curr_sum == 0 and curr_triplet not in result:
        #                 result.append(curr_triplet)
        #             elif curr_sum < 0:
        #                 j += 1
        #             else:
        #                 k -= 1
        

        # try 2 - more optimized (w/ help)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue    # skip if value at i is same as previous (not new)

            j = i + 1
            k = len(sorted_nums) - 1

            while j < k:
                curr_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                else: # = 0
                    result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    
                    j += 1
                    while sorted_nums[j] == sorted_nums[j - 1] and j < k:
                        j += 1  # inc j to skip duplicate elems
        
        return result
                    








                    







