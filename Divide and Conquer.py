#1.Construct Binary Tree from Preorder and inorder Traversal. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root=TreeNode()
        root.val=preorder[0]
        mid=inorder.index(root.val)
        root.left=self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root

#2.Construct Binary Tree from Inorder and Postorder traversal. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        root=TreeNode()
        root.val=postorder[-1]
        mid=inorder.index(root.val)
        root.left=self.buildTree(inorder[0:mid],postorder[:mid])
        root.right=self.buildTree(inorder[mid+1:],postorder[mid:-1])
        return root

#3.Convert Sorted Array to Binary search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root

#4.Convert Sorted List to Binary search Tree.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        def find_mid(start,end):
            slow=start
            fast=start
            while fast!=end and fast.next!=end:
                slow=slow.next
                fast=fast.next.next
            return slow
        def convertToBST(start,end):
            if start==end:
                return None
            mid=find_mid(start,end)
            root=TreeNode(mid.val)
            root.left=convertToBST(start,mid)
            root.right=convertToBST(mid.next,end)
            return root
        return convertToBST(head,None)

#5.Construct Binary Tree from Preorder and Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not postorder:
            return None
        root=TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        left_val=preorder[1]
        left_subtree_size=postorder.index(left_val)+1
        root.left=self.constructFromPrePost(preorder[1:left_subtree_size+1],postorder[0:left_subtree_size])
        root.right=self.constructFromPrePost(preorder[left_subtree_size+1:],postorder[left_subtree_size:-1])
        return root

#6. Maximum Sum Circular Subarray.

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_current=max_global=nums[0]  
            for i in range(1,len(nums)):
                max_current=max(nums[i],max_current+nums[i])
                max_global=max(max_global,max_current)
            return max_global 
        max_linear=kadane(nums)
        total_sum=sum(nums)
        max_wrap=total_sum+ kadane([-x for x in nums])
        return max(max_linear,max_wrap) if max_wrap!=0 else max_linear
        
#7.Kadane ALgorithm
def kadane(A):
    max_current=max_global=A[0]
    for i in range(1,len(A)):
        max_current=max(A[i],max_current+A[i])
        max_global=max(max_global,max_current)
    return max_global
A=[-1,2,-3,0,-2]
print(kadane(A))


