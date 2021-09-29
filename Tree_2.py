# 1. https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/ 108. Convert Sorted Array to Binary Search Tree
    def bst(self,nums,l,r):
        if l > r:
            return None
        m = (l+r)//2
        node = TreeNode(nums[m])
        node.left = self.bst(nums,l,m-1)
        node.right = self.bst(nums,m+1,r)
        return node
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.bst(nums,0,len(nums)-1)

# 2. https://leetcode.com/problems/balance-a-binary-search-tree/ - 1382. Balance a Binary Search Tree
    # Optimal - instead of storing val, we are storing the node itself
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node,arr):
            if node:
                inorder(node.left,arr)
                arr.append(node)
                inorder(node.right,arr)
        
        def arr_to_bbst(l,r):
            if l > r or len(arr) == 0:
                return None
            else:
                mid = (l+r)//2
                new_root = arr[mid]
                new_root.left = arr_to_bbst(l,mid-1)
                new_root.right = arr_to_bbst(mid+1,r)
                
                return new_root
        arr = []
        inorder(root,arr)
        return arr_to_bbst(0,len(arr)-1)

# 3. https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/ - 1038. Binary Search Tree to Greater Sum Tree
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        def reverseIorder(node, sum_):
            if not node:
                return sum_
            node.val += reverseIorder(node.right,sum_)
            return reverseIorder(node.left,node.val)
        reverseIorder(root,0)
        return root

# 4. https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/ - 1373. Maximum Sum BST in Binary Tree
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        result = [0]
        def maxbst(root):
            """Return sizeofbst, state_of_bst, leftmax,rightmin"""
            if not root:            # consider as bst
                return 0,True,-inf, inf  
            s1,bst1,max1,min1 = maxbst(root.left)
            s2,bst2,max2,min2 = maxbst(root.right)
            if bst1 and bst2 and max1 < root.val < min2:
                v  = root.val + s1 + s2
                result[0] = max(result[0], v)
                return v, True,max(root.val,max2), min(root.val,min1)
            return 0, False, -inf,inf # if not bst we reset it
        maxbst(root)
        return result[0]

# 5. https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/ - 108. Convert Sorted Array to Binary Search Tree
    def bst(self,nums,l,r):
        if l > r:
            return None
        m = (l+r)//2
        node = TreeNode(nums[m])
        node.left = self.bst(nums,l,m-1)
        node.right = self.bst(nums,m+1,r)
        return node
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.bst(nums,0,len(nums)-1)

# 6. https://leetcode.com/problems/validate-binary-search-tree/  - 98. Validate Binary Search Tree

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        res = []
        def inorder(root,res):
            if not root:
                return 
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
            return res
        inorder(root,res)  # inoder in BST always give sorted array
        n = len(res)
        for i in range(n-1):  # sorting 
            if res[i] >= res[i+1]:
                return False
        return True

# 7. https://leetcode.com/problems/recover-binary-search-tree/ -  99. Recover Binary Search Tree
    def inorder(self,root,arr):  # return sorted array of nodes
        if not root:
            return 
        self.inorder(root.left,arr)
        arr.append(root)
        self.inorder(root.right,arr)
        return arr
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        res = self.inorder(root,[])
        n = len(res)
                      
        a = res[0]      # setting default 1st wrong value as start
        for i in range(1,n):
            if res[i].val < res[i-1].val:
                a = res[i-1]
                break
            
        b = res[-1]   #setting default 1st wrong value as end
        for i in range(n-2,-1,-1):
            if res[i].val > res[i+1].val:
                b = res[i+1]
                break
        a.val,b.val = b.val,a.val       # swap

# 8. https://leetcode.com/problems/insert-into-a-binary-search-tree/ - 701. Insert into a Binary Search Tree
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        if root.val < val:
            root.right = self.insertIntoBST(root.right,val)
        else:
            root.left = self.insertIntoBST(root.left,val)
        return root

# 9. https://leetcode.com/problems/search-in-a-binary-search-tree/ - 700. Search in a Binary Search Tree
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def preorder(root):
            if root:
                if root.val == val:
                    return root
                elif root.val < val:
                    return preorder(root.right)
                else:
                    return preorder(root.left)
        return preorder(root) 


# 10. https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/ - 1008. Construct Binary Search Tree from Preorder Traversal
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

# 11. https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ - 235. Lowest Common Ancestor of a Binary Search Tree
    def LCA(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root.val < p.val and root.val < q.val:
            return self.LCA(root.right,p,q)
        elif root.val > p.val and root.val > q.val:
            return self.LCA(root.left,p,q)
        else:
            return root

