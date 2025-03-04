# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time O(n log k) k: number of sorted lists, n: total number of elements
# Space O(k)
from heapq import *
import math
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node: heappush(heap, (node.val, i, node)) # i is required if two objs have same priority then it considers i for comparison
        
        dummy = ListNode(-math.inf)
        curr = dummy
        while heap:
            nodeVal, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next != None: heappush(heap, (node.next.val, i, node.next))
        return dummy.next
        

# Time O(n*k)
# Space O(1)
from heapq import *
import math
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1: return lists[0]
        dummy = ListNode(-math.inf)
        curr = dummy
        p2 = lists[0]
        for item in lists[1:]:
            p1 = item
            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    p1 = p1.next
                else: 
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            if p1: 
                curr.next = p1
            if p2: 
                curr.next = p2
            p2 = dummy.next
            curr = dummy
        return dummy.next
        