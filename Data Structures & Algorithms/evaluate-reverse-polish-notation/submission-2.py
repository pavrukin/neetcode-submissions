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
            if char in operations:
                b=current_list.pop()
                a=current_list.pop()
                c=operations[char](a,b)
                current_list.append(c)
            else:
                current_list.append(int(char))

        return int(current_list[0])
