class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # iterate through grid
        # keep track of visited land
        # for each unvisited land, explore entire island -> return island area
        # update max if needed
        # continue

        maxArea = 0

        rows, cols = len(grid), len(grid[0])

        def explore(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] in (0, 2):
                return 0
            
            grid[r][c] = 2

            return 1 + explore(r + 1, c) + explore(r - 1, c) + explore(r, c + 1) + explore(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, explore(r, c))
        
        return maxArea