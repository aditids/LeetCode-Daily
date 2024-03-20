# 1669. Merge In Between Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        b = b-a
        prev = None
        cur = list1
        while a:
            a-=1
            prev = cur
            cur = cur.next
        
        ptail = None
        tail = list2
        while tail:
            ptail = tail
            tail = tail.next
        
        prev.next = list2
        while b:
            b-=1
            cur = cur.next
                   
        if cur and cur.next:
            ptail.next = cur.next
        else:
            ptail.next = cur

        return list1