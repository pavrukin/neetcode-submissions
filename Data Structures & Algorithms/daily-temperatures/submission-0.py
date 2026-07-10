class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        N=len(temperatures)
        result = [0] * N

        for index, temp in enumerate(temperatures):

            while stack and (stack[-1][0] < temp):
                print(" before pop", stack, "index", index, "temp", temp)
                k=stack.pop()[1]
                print(" after pop", stack)
                result[k]=index-k
            
            stack.append((temp,index))
        
        return result
        
