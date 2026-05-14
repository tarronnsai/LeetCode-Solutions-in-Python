# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list and find the tail
        length = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
            
        # 2. Normalize k
        k = k % length
        if k == 0:
            return head
        
        # 3. Connect the tail to the head to form a circle
        old_tail.next = head
        
        # 4. Find the new tail: (length - k - 1) steps from the start
        # The new head will be (length - k) steps from the start
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        
        # 5. Break the circle
        new_tail.next = None
        
        return new_head
        
#tarronnsaiadabala