class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
     set_of_num=set()
     set_of_lists=[[]]
     for i in nums:
        if i not in set_of_num:
            set_of_num.add(i)
            for j in set_of_lists.copy():
                # print("i",i,"j",j)
                new_element=j+[i]
                # print ("new_element", new_element)
                set_of_lists.append(new_element)
                # print("set_of_lists",set_of_lists) 

        
     return set_of_lists


        