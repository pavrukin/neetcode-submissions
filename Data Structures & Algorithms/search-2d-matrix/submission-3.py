class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up=0
        down=len(matrix)-1
        left=0
        right=len(matrix[0])-1

        while up<=down:
            position_row=(up+down)//2
            if matrix[position_row][0]==target:
                return True
            if matrix[position_row][-1]<target : up=position_row+1
            elif matrix[position_row][0]>target: down=position_row-1
            else: break
        
        position_row=(up+down)//2

        while left<=right:
            position_col=(left+right)//2
            if matrix[position_row][position_col]==target:
                return True
            if matrix[position_row][position_col]<target: left=position_col+1
            else: right=position_col-1
        return False


        

        