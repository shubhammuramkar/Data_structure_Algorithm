# 1. https://leetcode.com/problems/binary-tree-postorder-traversal/ - 145. Binary Tree Postorder Traversal
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        visited = set()
        stack = []
        result = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and not node.right in visited:
                    stack.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.val)
                    node = None
        return result

     ## Recussive approach    
    def pos(self,root,result):
        if not root:
            return root
        self.pos(root.left,result)
        self.pos(root.right,result)
        result.append(root.val)
        return result
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        result = []
        return self.pos(root,result)

#  2. https://leetcode.com/problems/binary-tree-inorder-traversal/ - 94. Binary Tree Inorder Traversal
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        stack = []
        result = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result




#  3. https://leetcode.com/problems/minimum-depth-of-binary-tree/ - 111. Minimum Depth of Binary Tree
    # level order / bfs
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = []
        q.append(root)
        depth = 1
        while len(q):
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth


    # DFS Approach 2
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right)) + 1

#  4. https://leetcode.com/problems/binary-tree-level-order-traversal/  - 102. Binary Tree Level Order Traversal
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        q,result = [],[]
        q.append(root)
        while len(q):
            l = []
            for _ in range(len(q)):
                node = q.pop(0)
                l.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            result.append(l)
        return result



#  5. https://leetcode.com/problems/maximum-depth-of-binary-tree/ - 104. Maximum Depth of Binary Tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1



#  6. https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/ - 103. Binary Tree Zigzag Level Order Traversal
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        stack, result = [],[]
        stack.append(root)
        leftToRight = True
        while len(stack):
            levelres = []
            nextlevel = []
            for _ in range(len(stack)):
                node = stack.pop()
                levelres.append(node.val)
                if leftToRight:
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
                else:
                    if node.right:
                        nextlevel.append(node.right)
                    if node.left:
                        nextlevel.append(node.left)
            stack = nextlevel
            result.append(levelres)
            leftToRight = not leftToRight
        return result





#  7. https://leetcode.com/problems/average-of-levels-in-binary-tree/ - 637. Average of Levels in Binary Tree
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return
        q = []
        result = []
        q.append(root)
        while len(q):
            l = 0
            n = len(q)
            for _ in range(len(q)):
                node = q.pop(0)
                l += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(l/n)
        return result



# 8. https://leetcode.com/problems/diameter-of-binary-tree/ - 543. Diameter of Binary Tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]   # global varibale
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2+left+right) # diamter
            
            return 1+max(left,right)  # height
        dfs(root)
        return res[0]
        
       
        
     # Solution 2   
    def diameter(self,root):
        if not root:
            return 0
        ld = self.diameter(root.left)
        rd = self.diameter(root.right)
        self.d = max(self.d, ld+rd)
        return max(ld,rd) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.diameter(root)
        return self.d



#  9. https://leetcode.com/problems/path-sum/ - 112. Path Sum
    # DFS using Recussive
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return 0
        def check(root,subpathsum,target):
            if not root:
                return 0
            if root.left == None and root.right == None:
                if subpathsum == target:
                    self.flag = True
            if root.left:
                check(root.left,subpathsum+root.left.val,target)
            if root.right:
                check(root.right,subpathsum+root.right.val,target)
        self.flag =False
        check(root,root.val,targetSum)
        return self.flag
    
    # DFS Using stack
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: 
        if not root:
            return 0
        stack = [(root,root.val)]
        while len(stack):
            node,sum_ = stack.pop()
            if node.left == None and node.right == None and sum_ == targetSum:
                return True
            if node.right:        # as right goes to bottom as stack is lifo
                stack.append((node.right,sum_+node.right.val))
            if node.left:
                stack.append((node.left,sum_+node.left.val))
        return False
     
    # BFS using Q
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: 
        if not root:
            return 0
        q = [(root,targetSum-root.val)]
        while len(q):
            node,rem = q.pop(0)
            if node.left == None and node.right == None and rem == 0:
                return True
            if node.left:
                q.append((node.left, rem-node.left.val))
            if node.right:
                q.append((node.right,rem-node.right.val))
        return False



#  10. https://leetcode.com/problems/path-sum-ii/ - 113. Path Sum II
    # DFS - recussion
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.check(root,targetSum,[],result)
        return result
        
    def check(self,root,target,path,res):
        if not root:
            return []
        if root.left == None and root.right == None and root.val == target:
            path.append(root.val)
            res.append(path)
        if root.left:
            self.check(root.left,target-root.val,path+[root.val],res)
        if root.right:
            self.check(root.right,target-root.val, path+[root.val],res)
            
    # DFS - Stack 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root,[root.val])]
        result = []
        while len(stack):
            node,ls = stack.pop()
            if node.left == None and node.right == None and sum(ls) == targetSum:
                result.append(ls)
            if node.right:
                stack.append((node.right,ls+[node.right.val]))
            if node.left:
                stack.append((node.left,ls+[node.left.val]))
        return result

   # BFS - using Q - I  
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = [(root,root.val,[root.val])]
        while len(q):
            node,sum_,ls = q.pop(0)
            if node.left == None and node.right == None and sum_ == targetSum:
                result.append(ls)
            if node.left:
                q.append((node.left,sum_+node.left.val, ls+[node.left.val]))
            if node.right:
                q.append((node.right,sum_+node.right.val, ls+[node.right.val]))
        return result
    
    # BFS - using Q - II
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = [(root,targetSum-root.val,[root.val])]
        while len(q):
            node,rem,ls = q.pop(0)
            if node.left == None and node.right == None and rem == 0:
                result.append(ls)
            if node.left:
                q.append((node.left,rem-node.left.val, ls+[node.left.val]))
            if node.right:
                q.append((node.right,rem-node.right.val, ls+[node.right.val]))
        return result



#  11. https://leetcode.com/problems/path-sum-iii/ - 437. Path Sum III
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        pathcount = 0
        stack[root]
        while len(stack):
            node = stack.pop()
            pathcount = self.pathcountSum(node,targetSum,pathcount)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return pathcount
    
    def pathcountSum(self,node,target,count):
        if not node:
            return count
        stack = [(node,node.val)]
        while len(stack):
            node,sum_ = stack.pop()
            if sum_ == target:
                count += 1
            if node.left:
                stack.append((node.left,sum_ + node.left.val))
            if node.right:
                stack.append((node.right,sum_ + node.right.val))
        return count
                

        
    # DFS - without prefix sum 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        stack = [root]
        pathcount = 0
        while len(stack):
            node = stack.pop()
            pathcount = self.pathcountSum(node,targetSum,pathcount)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return pathcount
    
    def pathcountSum(self,node,target,count):
        if not node:
            count
        stack = [(node,node.val)]
        while len(stack):
            node,sum_ = stack.pop()
            if sum_ == target:
                count += 1
            if node.left:
                stack.append((node.left,sum_+node.left.val))
            if node.right:
                stack.append((node.right,sum_+node.right.val))
        return count



#  12. https://leetcode.com/problems/distribute-coins-in-binary-tree/ - 979. Distribute Coins in Binary Tree
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        # traverse of dfs as post order - bottom up
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)            
            self.moves += abs(left) + abs(right)
            
            return node.val - 1 + left + right
        # -1 for itself, left,right as we need to further transfer to the parent if it exist
        dfs(root)
        return self.moves



#  13. https://leetcode.com/problems/path-sum-iv/ - 



#  14. https://leetcode.com/problems/sum-root-to-leaf-numbers/ - 129. Sum Root to Leaf Numbers
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        result = 0
        stack = [(root,root.val)]
        while len(stack):
            node,ls = stack.pop()
            if node.left == None and node.right == None:
                result += ls
            if node.left:
                stack.append((node.left,ls*10+node.left.val))
            if node.right:
                stack.append((node.right,ls*10+node.right.val))
        return result




#  15. https://leetcode.com/problems/longest-univalue-path/ - 687. Longest Univalue Path
   def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left == None or node.val != node.left.val:  
                left = 0                            # starting a new count
            if node.right == None or node.val != node.right.val:
                right = 0                           # starting a new count
            self.result = max(self.result,1+left+right) # +1 for node itself
            return 1 + max(left,right)
        dfs(root)
        return max(0,self.result-1)
    
    # Approach 2 
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal result
            
            if not node:
                return 0
            
            left = dfs(node.left)
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
                
            right = dfs(node.right)
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
                
            result = max(result, left+right)
            
            return max(left,right)
        result = 0
        dfs(root)      
        return result


# 16. https://leetcode.com/problems/subtree-of-another-tree/ - 572. Subtree of Another Tree
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(root,subroot):
            
            #if both are none
            if not root and not subroot: # mean root == None
                return True
            
            
            #if any one is none
            if not root or not subroot:
                return False
            
            # if node value is not same
            if root.val!=subroot.val:
                return False
            
            #node vaule is same and check of left and right part of subtree
            return dfs(root.left,subroot.left) and dfs(root.right,subroot.right)
        
        def solve(root,subroot):
            
            #if tree is empty return false
            if not root:
                return False
            
            #check if subtree exist in tree or not with root node same for both
            if dfs(root,subroot):
                return True
            
            #check of subtree in right and left subtree of tree
            return solve(root.left,subroot) or solve(root.right,subroot)
        return solve(root,subRoot)

## Approach 2
    def isSubtree(self, root: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_same(root,s):   # checking with root of tree
            return True
        return self.isSubtree(root.left,s) or self.isSubtree(root.right,s)  # either the subroot is in left half or right half
    
    def is_same(self,r,s):
        if r and s:
            return r.val == s.val and self.is_same(r.left,s.left) and         self.is_same(r.right,s.right)  
        return r is s
    
    ## "r is s" means "r == s", which smartly includes two conditions below:
# if r is None and s is None, return True
# if r is None or s is None, return False



# 17. https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ - 116. Populating Next Right Pointers in Each Node
    def connect(self, root: 'Node') -> 'Node':
        if root==None or root.left == None:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        else:
            root.right.next = None
        self.connect(root.left)
        self.connect(root.right)
        return root



# 18. https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/ - 117. Populating Next Right Pointers in Each Node II
    # Without extra space
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        head = root
        while head != None:
            dummy = Node(0)
            temp = dummy
            while head != None:
                if head.left:
                    temp.next = head.left
                    temp = temp.next
                if head.right:
                    temp.next = head.right
                    temp = temp.next
                head = head.next
            head = dummy.next
        return root
        
  # With extra space   
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = []
        q.append(root)
        while len(q):
            prev = None
            for _ in range(len(q)):
                curr = q.pop(0)
                if prev:
                    prev.next = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                prev = curr
        return root




# 19. https://leetcode.com/problems/maximum-width-of-binary-tree/ - 662. Maximum Width of Binary Tree
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [(root,1)]
        result = 1
        lastnode = root
        while len(q):
            node,index = q.pop(0)
            if node.left:
                q.append((node.left,2*index))  
            if node.right:
                q.append((node.right,2*index+1))
            if node == lastnode:
                if len(q):
                    result = max(result,q[-1][1] - q[0][1] + 1)
                    lastnode = q[-1][0]   # as we already have it in Q as once we are deleting the node from Q we are adding their child inside the Q
        return result



#  20.. https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/ - 987. Vertical Order Traversal of a Binary Tree
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        d = dict()
        vert,level = 0,0
        def function(root,vert,level):
            if not root:
                return
            if vert in d:
                d[vert].append((level,root.val))
            else:
                d[vert] = [(level,root.val)] 
            function(root.left,vert-1,level+1)
            function(root.right,vert+1,level+1)
        function(root,vert,level)
        # Struction of dict ={index:[level,value]}
        print(d)
        for i in sorted(d.keys()):
            temp = [j[1] for j in sorted(d[i])]
            res.append(temp)
        return res


