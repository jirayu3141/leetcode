from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None: return True

        allT = []
        self.get_height(root, allT)
        # print(allT)

        return all(allT)

    def get_height(self, curr, arr):
        if curr == None: return 0

        left = self.get_height(curr.left, arr)
        right = self.get_height(curr.right, arr)

        height = max(left, right) + 1 

        arr.append(abs(left - right) <= 1)

        return height

if __name__ == "__main__":
    # Tree: [3,9,20,null,null,15,7]
    '''
        3
       / \
      9  20
         / \
        15  7
        
    '''
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().isBalanced(root))


    

