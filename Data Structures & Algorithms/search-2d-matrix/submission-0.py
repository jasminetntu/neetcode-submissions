class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # r = 0
        # while r < len(matrix):
        #     if matrix[r][0] > target:
        #         return False
        #     elif matrix[r][len(matrix[r]) - 1] > target:
        #         r += 1
        #     else:
        #         i = 0
        #         j = len(matrix[r]) - 1

        #         while i < j:
        #             if i == target or j == target:
        #                 return True
        #             else:
        #                 i += 1
        #                 j -= 1
                
        #         r += 1
        

        i = 0
        j = len(matrix) - 1

        while i < j: # find row
            mid = (i + j) // 2
            
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            elif matrix[mid][0] > target:
                j = mid - 1
            else:
                i = mid + 1
        
        row = (i + j) // 2

        l = 0
        r = len(matrix[row]) - 1

        while l <= r: # find target in row
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
        

