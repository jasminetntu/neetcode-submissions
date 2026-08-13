class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = grid.copy()

        def explore(r, c):
            nonlocal visited
            
            if r < 0 or r >= len(visited) or c < 0 or c >= len(visited[0]): # outside bounds
                return
            if visited[r][c] == '0': # water
                return
            
            visited[r][c] = '0'

            explore(r, c + 1) # right
            explore(r, c - 1) # left
            explore(r + 1, c) # bot
            explore(r - 1, c) # top

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] == '1':
                    numIslands += 1
                    explore(r, c)

        return numIslands