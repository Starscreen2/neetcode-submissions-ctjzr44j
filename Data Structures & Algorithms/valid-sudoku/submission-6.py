class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for c in range(9):
            seen = set()
            for r in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                elif v in seen:
                    return False
                else:
                    seen.add(v)

        for r in range(9):
            seen = set()
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                elif v in seen:
                    return False
                else:
                    seen.add(v)
            
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen = set()
                for c in range(bc, bc + 3):
                    for r in range(br, br + 3):
                        v = board[r][c]
                        if v == ".":
                            continue
                        elif v in seen:
                            return False
                        else:
                            seen.add(v)
        return True
        