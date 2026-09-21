class Solution:
    from collections import deque
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        # if -1, we cant traverse -> return!!
        # 0, start
        # > 0, min(curr step, curr val)

        # def traverse(r, c, currStep):
        #     if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or currStep >= len(grid) * len(grid[0]):
        #         return

        #     if grid[r][c] < 0:
        #         return
            
        #     if grid[r][c] < currStep:
        #         return

        #     if grid[r][c]:
        #         grid[r][c] = min(grid[r][c], currStep)

        #     # print(r, c, currStep + 1)
        #     traverse(r + 1, c, currStep + 1)
        #     traverse(r - 1, c, currStep + 1)
        #     traverse(r, c + 1, currStep + 1)
        #     traverse(r, c - 1, currStep + 1)

        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    queue.append((r,c))

        currStep = 0
        while queue:
            # print(queue)
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                # if grid[r][c] < 0 or currStep > grid[r][c]:
                #     continue

                if r < len(grid)-1 and grid[r+1][c] > 0 and currStep + 1 < grid[r+1][c]:
                    grid[r+1][c] = min(grid[r+1][c], currStep + 1)
                    queue.append((r+1,c))
                if r > 0 and grid[r-1][c] > 0 and currStep + 1 < grid[r-1][c]:
                    grid[r-1][c] = min(grid[r-1][c], currStep + 1)
                    queue.append((r-1,c))
                if c < len(grid[0])-1 and grid[r][c+1] > 0 and currStep + 1 < grid[r][c+1]:
                    grid[r][c+1] = min(grid[r][c+1], currStep + 1)
                    queue.append((r,c+1))
                if c > 0 and grid[r][c-1] > 0 and currStep + 1 < grid[r][c-1]:
                    grid[r][c-1] = min(grid[r][c-1], currStep + 1)
                    queue.append((r,c-1))

            # for r in grid:
            #     print(r)
            # print()

            currStep += 1



                
            


