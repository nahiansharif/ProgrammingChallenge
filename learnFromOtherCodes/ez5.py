# https://leetcode.com/problems/symmetric-tree/description/

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). 

class Solution(object):
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    
from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        queue = deque([(root, root)])

        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True
    
class Solution:
    def isTreeSymmetric(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None:
            return True
        if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right) and self.isTreeSymmetric(leftRoot.right, rightRoot.left)
    def isSymmetric(self, root):
        return self.isTreeSymmetric(root.left, root.right)
    
    
class Solution(object):
    def isSymmetric(self, root):
        
        if not root:
            return True
        
        return self.isSame(root.left, root.right)
    
    def isSame(self, leftroot, rightroot):
        
        if leftroot == None and rightroot == None:
            return True
        
        if leftroot == None or rightroot == None:
            return False
        
        if leftroot.val != rightroot.val:
            return False
        
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
    
    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.symmetric(root.left, root.right) if root else True

    def symmetric(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:  
            return True
        if not root1 or not root2:   
            return False
        if root1.val != root2.val:  
            return False
        
        return self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right: 
                return False
            
            return left.val==right.val and dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)
