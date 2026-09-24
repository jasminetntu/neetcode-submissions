class Solution:
    from collections import deque

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c,1))
        
        while queue:
            r,c,nextStep = queue.popleft()
            
            # explore 4 directions
            if r + 1 < rows and grid[r + 1][c] > 0 and nextStep < grid[r + 1][c]:
                grid[r + 1][c] = nextStep
                queue.append((r + 1, c, nextStep + 1))
            if r - 1 >= 0 and grid[r - 1][c] > 0 and nextStep < grid[r - 1][c]:
                grid[r - 1][c] = nextStep
                queue.append((r - 1, c, nextStep + 1))
            if c + 1 < cols and grid[r][c + 1] > 0 and nextStep < grid[r][c + 1]:
                grid[r][c + 1] = nextStep
                queue.append((r, c + 1, nextStep + 1))
            if c - 1 >= 0 and grid[r][c - 1] > 0 and nextStep < grid[r][c - 1]:
                grid[r][c - 1] = nextStep
                queue.append((r, c - 1, nextStep + 1))
        