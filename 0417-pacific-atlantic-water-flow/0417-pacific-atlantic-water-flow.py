class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res=[]

        def dfs(r, c, prev_H, v_set):
            if r==ROWS or r<0 or c==COLS or c<0 or heights[r][c]<prev_H or (r,c) in v_set:
                return
            v_set.add((r,c))
            dfs(r+1, c, heights[r][c], v_set)
            dfs(r, c+1, heights[r][c], v_set)
            dfs(r-1, c, heights[r][c], v_set)
            dfs(r, c-1, heights[r][c], v_set)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS-1, c, heights[ROWS-1][c], atl)
            
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS-1, heights[r][COLS-1], atl)
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        
        return res