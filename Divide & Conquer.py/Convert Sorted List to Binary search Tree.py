
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
