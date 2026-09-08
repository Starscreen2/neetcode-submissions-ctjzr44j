class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # save the numebr of rows and cols
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        # go through every cell in the grid
        # if the cell is water, skip, else if its island cell, increase islands
        # dfs all of the connected land
        # change visited to water (0)
        # return the count

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            #stop outside the grid
            #stop at water or visited land
            if grid[row][col] == "0":
                return

            # mark this land as visited
            grid[row][col] = "0"

            #check all directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        #go through each row and col
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands










        