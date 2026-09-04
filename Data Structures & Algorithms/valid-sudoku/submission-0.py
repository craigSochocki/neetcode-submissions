class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        N_ROWS = 9
        N_COLS = 9

        def checkNums(nums: List[str]) -> bool:
            counts = set()
            for num in nums:
                if num in counts:
                    if num != '.':
                        print(f"nums {nums} ARE INVALID -- {num} repeated!")
                        return False
                else:
                    counts.add(num)
            return True

        def getRow(board: List[List[str]], n: int) -> List[str]:
            row = board[n]
            return row
        
        def getCol(board: List[List[str]], m: int) -> List[str]:
            col = []
            for row in board:
                col.append(row[m])
            return col
        
        def getBox(board: List[List[str]], starting_row: int, starting_col: int) -> List[List[str]]:
            width, height = 3,3
            box = []
            for row_index in range(starting_row, starting_row + height):
                box.append(getRow(board, row_index)[starting_col:starting_col+width])
            
            return box

        def checkRow(row_num: int) -> bool:
            row = getRow(board, row_num)
            return checkNums(row)

        def checkColumn(col_num: int) -> bool:
            col = getCol(board, col_num)
            return checkNums(col)
        
        def checkBox(starting_row:int, starting_col:int) -> bool:
            box = getBox(board,starting_row,starting_col)
            
            nums = []
            for row in box:
                nums.extend(row)

            return checkNums(nums)

        def checkAllBoxes() -> bool:
            row_index = 0

            while row_index <= 6:
                col_index = 0
                while col_index <=6:
                    is_valid = checkBox(row_index, col_index)
                    if not is_valid:
                        print("BOX IS INVALID")
                        return False
                    col_index += 3
                row_index +=3
            return True
        
        isValid = True
        row_num = 0
        while row_num < N_ROWS and isValid:
            isValid = checkRow(row_num)
            row_num += 1
        
        col_num = 0
        while col_num < N_COLS and isValid:
            isValid = checkColumn(col_num)
            col_num += 1

        if isValid:
            isValid = checkAllBoxes()

        return isValid
