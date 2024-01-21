from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            
            for _ in range(level_length):
                node, col_index = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))
            
            max_width = max(max_width, col_index - level_head_index + 1)
        
        return max_width

def list_to_binarytree(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    n = iter(nums)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = TreeNode(next(n))
            fringe.append(head.left)
            head.right = TreeNode(next(n))
            fringe.append(head.right)
        except StopIteration:
            break
    return tree

# Checking in terminal/console:
if __name__ == '__main__':

    assert Solution().widthOfBinaryTree(list_to_binarytree([1,3,2,5,3,None,9])) == 4
    assert Solution().widthOfBinaryTree(list_to_binarytree([1,3,None,5,3])) == 2
    assert Solution().widthOfBinaryTree(list_to_binarytree([1,3,2,5])) == 2
    assert Solution().widthOfBinaryTree(list_to_binarytree([1,3,2,5,None,None,9,6,None,None,None,None,None,None,7])) == 8
    assert Solution().widthOfBinaryTree(list_to_binarytree([1,3,2,5,None,None,9,6,None,None,7,None,None,None,None,8])) == 8

    print("All tests passed successfully.")
