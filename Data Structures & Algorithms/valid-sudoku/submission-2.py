class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking process:
        #   Make a frequency dictionary and whenever incremented, if the new value
        #   is >1 then the whole sudoku is invalid
        #1. Check all 3x3 sub-boxes
        for i in range(3):
            rows = board[(i*3):(i+1)*3 ] # first get the rows
            
            for j in range(3):
                box = [row[(j*3):(j+1)*3] for row in rows] # then get cols (now should be 3x3)
                box_freq =defaultdict(int)
                for box_row in box:
                    for val in box_row:
                        box_freq[val] +=1
                        if val != "." and box_freq[val] > 1:
                            return False
        #2. Check all rows
        #3. Can also construct columns while going over rows
        cols = [[] for _ in range(9)]
        
        for i in range(9):
            row  = board[i]
            row_freq = defaultdict(int)
            for j,val in enumerate(row):
                row_freq[val]+=1
                if val != "." and row_freq[val] > 1:
                    return False
                cols[j].append(val)
        #3. Check all columns
        for i in range(9):
            col  = cols[i]
            col_freq = defaultdict(int)
            for val in col:
                col_freq[val]+=1
                if val != "." and col_freq[val] > 1:
                    return False
        return True