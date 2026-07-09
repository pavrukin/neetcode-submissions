class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
            }

        current_list=[]

        for char in tokens:
            #print('char',char)
            if char in operations:
                b=current_list.pop()
                #print("after pop 1", current_list)
                a=current_list.pop()
                #print("after pop 2", current_list)
                c=operations[char](a,b)
                current_list.append(c)
                #print("after add c", current_list)
            else:
                current_list.append(int(char))



        return int(current_list[0])
