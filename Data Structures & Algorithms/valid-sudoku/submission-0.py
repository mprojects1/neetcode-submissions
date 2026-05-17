class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for l in board:
            map = {}
            for i in l:
                if i != '.':
                    map[i] = map.get(i,0) + 1
            for value in map.values():
                if value > 1: return False
        
        j = 0

        while j < 9:
            i = 0
            map = {}
            while i < 9:
                if board[i][j] != '.':
                    map[board[i][j]] = map.get(board[i][j], 0) + 1
                i +=1
            for value in map.values():
                if value > 1: return False 
            j += 1

        
        for r in range(0,9,3):
            for c in range(0,9,3):

                seen = set()

                for i in range(3):
                    for j in range(3):
                        
                        cell = board[r+i][c+j]

                        if cell != '.':
                            if cell in seen:
                                return False
                            else: seen.add(cell)
        return True
