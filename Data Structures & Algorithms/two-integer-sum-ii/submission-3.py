class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        finish = len(numbers) - 1
   
        while start < finish:
            current_sum = numbers[start] + numbers[finish]
        
            if current_sum == target:
                return [start + 1, finish + 1]
            elif current_sum > target:
                finish -= 1
            else:
                start += 1

    # return [0,0]  # if no pair is found    