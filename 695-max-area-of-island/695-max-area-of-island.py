def dfs(grid, x, y, visited, m, n):
    
    dx = [0, 1, 0, -1]
    df = [1, 0, -1, 0]

    visited[x][y] = True
    area = 1
    for i in range(4):
        xi = x + dx[i]
        yi = y + df[i]

        if xi>= 0 and xi<m and yi>=0 and yi<n and grid[xi][yi] ==  1 and (not visited[xi][yi]):
            area += dfs(grid, xi, yi, visited, m, n) 
    return area
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        print(len(visited), len(visited[0]))
        print(len(grid), len(grid[0]))
        max_area = 0
        for x in range(m):
            for y in range(n):
                if (not visited[x][y]) and grid[x][y] == 1: 
                    area = dfs(grid, x, y, visited, m, n)
                    if max_area < area:
                        max_area = area
        return max_area