class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        time = 0

        # while there are fresh oranges
        # for all the rotten oranges, make the fresh ones next to them rotten 
        # increase time by 1
        # decrease number of fresh oranges

        # check at beginning of while loop
        # if prev # of fresh oranges = curr number of fresh oranges
        # we know that it's impossible to reach the remaining fresh
        # so return -1

        fresh = 0
        rotten = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1 
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        while len(rotten) > 0 and fresh > 0:
            # print(time, fresh, rotten)
            
            new = []

            while len(rotten) > 0:
                r,c = rotten.pop(0)
                if r + 1 < m and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2 
                    new.append((r + 1, c))
                    fresh -= 1
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    new.append((r - 1, c))
                    fresh -= 1
                if c + 1 < n and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    new.append((r, c + 1))
                    fresh -= 1
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    new.append((r, c - 1))
                    fresh -= 1
            
            time += 1
            rotten = new

        if fresh > 0:
            return -1
        return time