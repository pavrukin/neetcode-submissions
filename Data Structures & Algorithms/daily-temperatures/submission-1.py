class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        N=len(temperatures)
        result = [0] * N

        for index, temp in enumerate(temperatures):
            # from current element look back to check if there is the one with lower temperature
            while stack and (stack[-1][0] < temp):
                print(" before pop", stack, "index", index, "temp", temp)
                # as we found the lower temperature by index it is already minimum so we don't need it further
                k=stack.pop()[1]
                print(" after pop", stack)
                # as result[k] is defined it will not be rewritten
                result[k]=index-k
                # it will go further if the current temperature is higher than 2-3 and more indexes back
            
            stack.append((temp,index))
        
        return result
        
