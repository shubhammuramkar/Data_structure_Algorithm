# 1. https://leetcode.com/problems/reorder-list/ - 143. Reorder List
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        if not head.next:
            return head
        fast = head
        slow = head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None          # left half last node = None
        prev = None
        while slow:            # reverse of other half of LL 
            n = slow.next
            slow.next = prev
            prev = slow
            slow = n         
        rev_head = prev  # head of the reverse list        
        temp = head
        while temp:      # joining as per condtition
            n1 = temp.next
            temp.next = rev_head
            n2 = rev_head.next
            rev_head.next = n1
            temp = n1
            rev_head = n2
            
        temp1 = head           
        if rev_head:  # list is even,need to join last node of rev list to main list
            while temp1.next:
                temp1 = temp1.next
            temp1.next = rev_head
        return head




#  2. https://leetcode.com/problems/merge-two-sorted-lists/  - 21. Merge Two Sorted Lists
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # for pointing to the sorted list that are making 
        temp = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  # if any l1 or l2 = None temp point to the remaning list
        return dummy.next     # as dummy point to 0 define initially

# 3. https://leetcode.com/problems/linked-list-cycle/ - 141. Linked List Cycle
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        p = head
        q = head.next
        while p != None and q.next != None:
            p = p.next
            q = q.next.next
            if p == q:
                return True
            if q == None:
                return False
        return False



#  4. https://leetcode.com/problems/linked-list-cycle-ii/ - 142. Linked List Cycle II
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next          
            if slow == fast:
                break   
                # For removing the cycle and find the lenght of cycle
                #   
                # count = 1
                # while fast.next != slow:
                #     count += 1
                #     fast = fast.next
                # fast.next = None
                
        if slow == fast:
            while head != fast:
                fast = fast.next
                head = head.next
            return head
        else:
            return None

# 5. https://leetcode.com/problems/next-greater-node-in-linked-list/ - 1019. Next Greater Node In Linked List
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
            if not head:
                return head
            arr = []
            while head:
                arr.append(head.val)
                head = head.next         
            n = len(arr)
            stack = []
            result = [0]*n
            for i in range(n-1,-1,-1):
                while len(stack):
                    s = stack.pop()
                    if s <= arr[i]:
                        continue
                    else:
                        result[i] = s
                        stack.append(s)
                        stack.append(arr[i])
                        break
                if len(stack) == 0:
                    stack.append(arr[i])
                    result[i] = 0
            return result    

#  6. https://leetcode.com/problems/swap-nodes-in-pairs/ - 24. Swap Nodes in Pairs
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d1 = d = ListNode(0)
        d.next = head
        while d.next and d.next.next:
            p = d.next
            q = d.next.next
            d.next = q
            p.next = q.next
            q.next = p        # d.next,p.next,q.next = q, q.next, p
            d = p
        return d1.next

#  7. https://leetcode.com/problems/rotate-list/ - 61. Rotate List
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k <= 0:
            return head
        temp = head
        count = 0
        while temp.next:
            temp = temp.next
            count += 1
        count += 1
        if k % count == 0:
            return head
        if k > count:
            s = k % count  # to start from 0
            n = count-s
        else:
            n = count-k           
        q = head
        temp.next = head
        for _ in range(n-1):
            q = q.next
        t = q.next
        q.next = None
        return t

# 8. https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ -82. Remove Duplicates from Sorted List II
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.next != None and head.val == head.next.val:
                while head.next != None and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:   
                prev = prev.next
            head = head.next
        return dummy.next  

#  9. https://leetcode.com/problems/next-greater-node-in-linked-list/ - 1019. Next Greater Node In Linked List
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
            if not head:
                return head
            arr = []
            while head:
                arr.append(head.val)
                head = head.next         
            n = len(arr)
            stack = []
            result = [0]*n
            for i in range(n-1,-1,-1):
                while len(stack):
                    s = stack.pop()
                    if s <= arr[i]:
                        continue
                    else:
                        result[i] = s
                        stack.append(s)
                        stack.append(arr[i])
                        break
                if len(stack) == 0:
                    stack.append(arr[i])
                    result[i] = 0
            return result               

# 10. https://leetcode.com/problems/odd-even-linked-list/ - 328. Odd Even Linked List
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        oddhead = head
        oddtail = head
        evenhead = head.next
        eventail = head.next
        while eventail != None and eventail.next != None:
            oddtail.next = oddtail.next.next
            eventail.next = eventail.next.next
            oddtail = oddtail.next
            eventail = eventail.next
        oddtail.next = evenhead
        return oddhead

# 11. https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/ - primium

# 12. https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/ - 82. Remove Duplicates from Sorted List II
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.next != None and head.val == head.next.val:
                while head.next != None and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:   
                prev = prev.next
            head = head.next
        return dummy.next 

# 13. https://leetcode.com/problems/add-two-numbers-ii/ - 445. Add Two Numbers II
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = self.reverse(l1)
        head2 = self.reverse(l2)
        return self.reverse(self.addlist(head1,head2))

    def reverse(self,l1):
        prev = None
        while l1 != None:
            n = l1.next
            l1.next = prev
            prev = l1
            l1 = n
        return prev
    
    def addlist(self,l1,l2):
        carry = 0
        head1 = l1
        head2 = l2
        dummy_node = ListNode(0)
        dummy_head = dummy_node
        while head1 != None and head2 != None:
            result = head1.val + head2.val + carry
            digit = result % 10
            carry = int(result / 10)
            new_node = ListNode(digit)
            dummy_node.next = new_node
            dummy_node = dummy_node.next
            head1 = head1.next
            head2 = head2.next
            
        # If both LL is of same length            
        if head1 == None and head2 == None and carry > 0:
            dummy_node.next = ListNode(carry)
            
        # if LL1 is greater 
        while head1 != None and head2 == None:
            if carry > 0:
                result = head1.val + carry
                digit = result % 10
                carry  = int(result / 10)
                print(result,digit,carry)
                new_node = ListNode(digit)
                dummy_node.next = new_node
                dummy_node = dummy_node.next
            else:
                new_node = ListNode(head1.val)
                dummy_node.next = new_node
                dummy_node = dummy_node.next
            head1 = head1.next
            if head1 == None:
                if carry > 0:
                    dummy_node.next = ListNode(carry)
                    
        # if LL2 is greater
        while head2 != None and head1 == None:
            if carry > 0:
                result = head2.val + carry
                digit = result % 10
                carry  = int(result / 10)
                new_node = ListNode(digit)
                dummy_node.next = new_node
                dummy_node = dummy_node.next
            else:
                new_node = ListNode(head2.val)
                dummy_node.next = new_node
                dummy_node = dummy_node.next
            head2 = head2.next
            if head2 == None:
                if carry > 0:
                    dummy_node.next = ListNode(carry)
        return dummy_head.next

# 14. https://leetcode.com/problems/reverse-nodes-in-k-group/ - 25. Reverse Nodes in k-Group
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
            
        d = ListNode(0,head)
        gp = d
        while True:
            kth = self.getk(gp, k)
            if not kth:
                break
            groupnext = kth.next
            
            # Reverse
            prev = kth.next
            curr = gp.next
            while curr != groupnext:
                temp  = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = gp.next
            gp.next = kth
            gp = tmp
        return d.next
    
    def getk(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


#  15. https://leetcode.com/problems/copy-list-with-random-pointer/ - 138. Copy List with Random Pointer
   def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        temp = head
        while temp:
            node = Node(temp.val)
            n = temp.next
            temp.next = node
            node.next = n
            temp = n
        
        temp1 = head
        while temp1 != None:
            if temp1.random == None:
                temp1.next.random = None
            else:
                temp1.next.random = temp1.random.next
            temp1 = temp1.next.next
        
        p = head.next
        rtemp = p
        while p != None and p.next != None:
            p.next = p.next.next
            p = p.next
            
        return rtemp

# 16. https://leetcode.com/problems/reverse-linked-list/ - 206. Reverse Linked List
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            n = head.next
            head.next = prev
            prev = head
            head = n
        return prev

#  17. https://leetcode.com/problems/intersection-of-two-linked-lists/ -  160. Intersection of Two Linked Lists
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Counting the no. of node in headA
        temp = headA  
        count1 = 0
        while temp:
            count1 += 1
            temp = temp.next
        # Counting the no. of node in headB
        count2 = 0
        temp = headB
        while temp:
            count2 += 1
            temp = temp.next
          
        # based on which one is greater we are shifting the pointer to diff. of 2
        if count1 > count2:
            shift = count1-count2
            tempA = headA
            tempB = headB
            for _ in range(shift):  # shifting
                tempA= tempA.next
                
            while tempB and tempA:  # now comparing weather the node is same..?
                if tempB == tempA:
                    return tempB
                tempA = tempA.next
                tempB = tempB.next
        else:
            shift = count2-count1
            tempB = headB
            tempA = headA
            for _ in range(shift):
                tempB = tempB.next
            while tempB and tempA:
                if tempB == tempA:
                    return tempB
                tempA = tempA.next
                tempB = tempB.next
        return None                # No common node
         
        
        
        ## Bruteforce 1
#         temp = headA
#         arr = []
#         while temp:
#             arr.append(temp)
#             temp = temp.next
#         while headB:
#             if headB in arr:
#                 return headB
#             headB = headB.next
#         return None

        
        
        ## Bruteforce 2
        # n = headA
        # while headB:
        #     while headA:
        #         if headA == headB:
        #             return headA
        #         headA = headA.next
        #     headA = n
        #     headB = headB.next
        # return None