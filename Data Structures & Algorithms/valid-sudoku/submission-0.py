class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # only look at existing values, NOT solving
        
        # each list in board list must contain only unqiue values (rows)
        # each index in board list must contain only unique values (cols)
        # each 3x3 in board list must contain only unique values

        # iterate through each cell
        # keep track of each r,c,b for unique values
        # if anything is repeating, return false immediately

        # TRY 1
        # from collections import defaultdict

        # unique = defaultdict(list)
        
        # for r in range(len(board)):
        #     for c in range(len(board[r])):
        #         if board[r][c] == '.': # skip cell if empty
        #             continue

        #         if board[r][c] not in unique['r' + str(r)]:
        #             unique['r' + str(r)].append(board[r][c]) # add to row
        #         else:
        #             return False
                
        #         if board[r][c] not in unique['c' + str(c)]:
        #             unique['c' + str(c)].append(board[r][c]) # add to col
        #         else:
        #             return False
                
        #         br = str(r // 3)
        #         bc = str(c // 3)
        #         if board[r][c] not in unique['b' + br + bc]:
        #             unique['b' + br + bc].append(board[r][c]) # add to box
        #         else:
        #             return False
                
                # r5 c4 -> 5 // 3 = 1, 4 // 3 = 1 -> b5
                # r2 c4 -> 2 // 3 = 0, 4 // 3 = 1 -> b2
                # r1 c2 -> 0, 0 -> b1
                # r7 c2 -> 2, 0 -> b7
                # r6 c6 -> 2, 2 -> b9

                # time: O(n^2)



        # TRY 2 - instead of dict, let's try using array for faster lookup
        
        # initialize 9x9 2d array list[i][j]
        # where i = row/col/box ind & j = value
        # indices -> 0 to 8
        row = [[0] * 9 for _ in range(9)] 
        col = [[0] * 9 for _ in range(9)]
        box = [[0] * 9 for _ in range(9)]
        
        # iterate through board
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.': # skip cell if empty
                    continue

                currVal = int(board[r][c]) - 1 # turn value into int

                if row[r][currVal] == 0: # not in row yet
                    row[r][currVal] = 1
                else:
                    return False
                
                if col[c][currVal] == 0: # not in col yet
                    col[c][currVal] = 1
                else:
                    return False
                
                # get unique box index - row * number_of_columns + column
                b = (r // 3) * 3 + (c // 3) 

                # print(r, c, b)
                
                if box[b][currVal] == 0: # not in box yet
                    box[b][currVal] = 1
                else:
                    return False

        return True

