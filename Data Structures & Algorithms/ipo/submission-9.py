class Solution:
    import heapq
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects=list(zip(capital,profits))
        heapq.heapify(projects)
        max_profit_heap=[]
        
        for _ in range(k):
            # existing projects and checking entrance capital
            while projects and projects[0][0]<=w:
                #extract by capital
                cap, prof = heapq.heappop(projects)
                #create max by profit using negative values
                heapq.heappush(max_profit_heap,(-prof,cap))
            if not max_profit_heap:
                break
            # print("max_profit_heap",max_profit_heap)
        
            current_max_profit, _ =heapq.heappop(max_profit_heap)
            w+= -current_max_profit

        return w
            