class Solution:
    def subsets(self, nums):
     set_of_num=set()
     set_of_lists=[[]]
     for i in nums:
        if i in set_of_num:
            pass
        else:
            set_of_num.add(i)
            for j in set_of_lists.copy():
                new_element=j+[i]
                set_of_lists.append(new_element)       
     return set_of_lists


        