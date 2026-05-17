class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()
        for r in range(9):
            for c in range(9):

                cell = board[r][c]

                if cell == '.':
                    continue

                row_key = f"r{r}:{cell}"
                col_key = f"c{c}:{cell}"
                sub_key = f"s{r//3},{c//3}:{cell}"

                if row_key in seen or col_key in seen or sub_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(sub_key)
        return True

