class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current_list = []
        for char in tokens:
            if char =="+":
                current_list.append(current_list.pop()+current_list.pop())
            elif char =="*":
                current_list.append(current_list.pop()*current_list.pop())
            elif char =="-":
                current_list.append(-current_list.pop()+current_list.pop())
            elif char =="/":
                current_list.append(int(1/current_list.pop()*current_list.pop()))
            else:
                current_list.append(int(char))

        return int(current_list[0])