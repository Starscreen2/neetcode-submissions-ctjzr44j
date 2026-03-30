class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for r in range(9):
            seen = []
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.append(v)

        # check cols
        for c in range(9):
            seen = []
            for r in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.append(v)

        # check 3x3 boxes
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen = []
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        v = board[r][c]
                        if v == ".":
                            continue
                        if v in seen:
                            return False
                        seen.append(v)

        return True