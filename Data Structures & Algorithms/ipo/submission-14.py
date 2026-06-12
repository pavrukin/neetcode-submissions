import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        
        # 1. Create an array of indices [0, 1, 2, ..., n-1]
        # Sort these indices based on the capital required for each project
        # This avoids zipping and creating thousands of tuple objects!
        indices = sorted(range(n), key=lambda i: capital[i])
        
        max_profit_heap = []
        project_ptr = 0  # A pointer to track which projects we've looked at
        
        for _ in range(k):
            # 2. Instead of popping from a list, we just move our pointer forward.
            # This is an incredibly fast O(1) index lookup.
            while project_ptr < n and capital[indices[project_ptr]] <= w:
                # Push ONLY the profit (as a negative number). 
                # We don't need the capital anymore since we already know we can afford it!
                heapq.heappush(max_profit_heap, -profits[indices[project_ptr]])
                project_ptr += 1
                
            if not max_profit_heap:
                break
                
            # 3. Pop the max profit and add it to our capital
            w += -heapq.heappop(max_profit_heap)
            
        return w
            