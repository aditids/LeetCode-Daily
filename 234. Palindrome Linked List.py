# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        k = []
        while fast and fast.next:
            k.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        for i in range(len(k)-1,-1,-1):
            if slow and slow.val==k[i]:
                slow = slow.next
                continue
            return False                        
        
        return True