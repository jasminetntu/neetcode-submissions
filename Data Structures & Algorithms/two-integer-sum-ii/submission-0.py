class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted asc
        # x + y = target
        # add 1 to indices

        # for 2 ptr, avoid for loop -> use while loop

        # TRY 1 - brute force
        # for i in range(len(numbers)):
        #     x = numbers[i]

        #     for j in range(i + 1, len(numbers)):
        #         y = numbers[j]

        #         if x + y == target:
        #             return [i + 1, j + 1]
        

        # TRY 2 - with while loop
        # i = 0
        # j = 1

        # while j < len(numbers): # i < len(numbers) not needed to check
        #     if numbers[i] + numbers[j] == target:
        #         return [i + 1, j + 1]
            
        #     if numbers[j] > target or j == len(numbers) - 1:
        #         i += 1
        #         j = i + 1
        #     else:
        #         j += 1


        # TRY 3 - with while & going from both ends
        i = 0
        j = len(numbers) - 1

        while i < j: 
            currSum = numbers[i] + numbers[j]

            if currSum == target:
                return [i + 1, j + 1]
            elif currSum > target:
                j -= 1
            else: # currSum < target
                i += 1

        return [-1, -1] # will never be hit