class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        #empty grid
        #create set for cell that are reachable from the pacific ocean
        #create set for cell that are reachable from the atlantic ocean
        #run dfs from all pacific boarder cells
        #run dfs from all atlantic boarder cells
        #return the calls found in both sets

        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])    
        pacific, atlantic = set(), set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        #dfs algo 
        def dfs(r, c, reachable):
            if(r,c) in reachable:
                return
            reachable.add((r,c))
        #try all 4 directions of the neighboring cells
            for dr, dc, in directions:
                nr = r + dr
                nc = c + dc
                
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in reachable
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, reachable)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result

