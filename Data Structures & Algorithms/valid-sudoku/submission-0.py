class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        already_added=set()

        for i in range(9):
            for j in range(9):

                num=board[i][j]

                if num==".": continue

                col_key=f"col_{j}_num_{num}"
                row_key=f"row_{i}_num_{num}"
                cube_key=f"col_{j//3}_row_{i//3}_num_{num}"

                if (col_key in already_added
                    or row_key in already_added
                    or cube_key in already_added): return False

                else:
                    already_added.add(col_key)
                    already_added.add(row_key)
                    already_added.add(cube_key)
        return True
