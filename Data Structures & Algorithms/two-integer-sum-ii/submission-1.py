class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        finish=len(numbers)-1
       
        while start<finish:
            if numbers[start]+numbers[finish]==target:
                break
            elif numbers[start]+numbers[finish]>target:
                finish-=1
            else: start+=1

        print(start,finish)
        if start<finish:
            return[start+1,finish+1]
        else:
            return [0,0]