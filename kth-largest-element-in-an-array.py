# Time O(n log k)
# Space O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        count = 0
        for num in nums:
            heapq.heappush(hq, num)
            count += 1
            if count > k:
                heapq.heappop(hq)
                count -= 1
        return heapq.heappop(hq)
    
# Time O(n log n-k)
# Space O(n-k)
from heapq import *
import math
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        count = 0
        n = len(nums)
        res = -math.inf
        for num in nums:
            heappush(hq, -num)
            count += 1
            if count > (n - k):
                res = max(res, heappop(hq))
                count -= 1
        return -res
        
        