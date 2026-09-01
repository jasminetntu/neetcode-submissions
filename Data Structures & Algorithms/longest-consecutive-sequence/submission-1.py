class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest = 1
        numSet = set(nums)

        for i in numSet:
            if i - 1 not in numSet and i + 1 in numSet:
                curr = 0
                j = i
                while j in numSet:
                    curr += 1
                    j += 1
                longest = max(longest, curr)
                

        # sortedNums = sorted(list(set(nums))) # O(nlogn) -> not O(n)

        # i = 0
        # j = 1
        # while i < j and j < len(sortedNums):
        #     # print(sortedNums[i], sortedNums[j])
        #     if sortedNums[j] != sortedNums[j - 1] + 1:
        #         i = j
        #         j = i + 1
        #     else:
        #         j += 1
        #         longest = max(longest, j - i)

        return longest