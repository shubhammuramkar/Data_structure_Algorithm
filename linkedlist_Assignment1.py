#1. 19. Remove Nth Node From End of List  - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return -1
        if not head.next:
            if n == 1:
                return None
            elif n == 0:
                return head
            else:
                return -1
        p = head
        q = head
        prev = None  # storing the prev pointer 
        for _ in range(n):
            q = q.next
        if q == None:  # removing the 1st node
            p = p.next
            return p 
        while q.next:   # find the nth last node while q reached last p is standing just before the node that we need to delete
            p = p.next
            q = q.next
        prev = p
        p = p.next
        prev.next = p.next

        return head
        
#2. 876. Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

#3. 237. Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """  
        node.val = node.next.val        # puting the next element to current val i.e overlapping till the end
        node.next = node.next.next

#4. 203. Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        while head:       # if the head value is = val
            if head.val == val:
                head = head.next
            else:
                break     # to come out of while loop
        prev = None
        temp = head
        while temp != None:
            if temp.val != val:   # just updating the temp and prev
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next   # deleting the node
                temp = temp.next 
        return head
    
# 5. https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/ - premium Q

#6. 1171. Remove Zero Sum Consecutive Nodes from Linked List - https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
doubt
