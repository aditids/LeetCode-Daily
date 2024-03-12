# 1171. Remove Zero Sum Consecutive Nodes from Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = dummy
        hmap = {}
        prefix_sum = 0
        
        while cur:
            prefix_sum+=cur.val
            if prefix_sum in hmap:
                temp_sum = prefix_sum
                k = hmap[prefix_sum]
                temp = k.next
                while temp!=cur:
                    temp_sum+=temp.val
                    del hmap[temp_sum]
                    temp = temp.next
                k.next = cur.next
                cur = cur.next
            else:
                hmap[prefix_sum] = cur
                cur = cur.next
        return dummy.next