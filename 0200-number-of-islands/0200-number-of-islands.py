class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        v_set = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if j+1<cols and grid[i][j+1]=="1" and (i, j+1) not in v_set:
                v_set.add((i, j+1))
                dfs(i, j+1)
            if j-1>-1 and grid[i][j-1]=="1" and (i, j-1) not in v_set:
                v_set.add((i, j-1))
                dfs(i, j-1)
            if i+1<rows and grid[i+1][j]=="1" and (i+1, j) not in v_set:
                v_set.add((i+1, j))
                dfs(i+1, j)
            if i-1>-1 and grid[i-1][j]=="1" and (i-1, j) not in v_set:
                v_set.add((i-1, j))
                dfs(i-1, j)
            return 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i, j) not in v_set:
                    v_set.add((i, j))
                    dfs(i, j)
                    ans+=1
        return ans


