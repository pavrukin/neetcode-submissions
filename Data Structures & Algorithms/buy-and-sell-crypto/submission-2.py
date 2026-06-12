from itertools import accumulate
import numpy as np
class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_diff=0
        for i in prices:
            if min_price>i : min_price=i
            diff=i-min_price
            if max_diff<diff: max_diff=diff
        return max_diff

        