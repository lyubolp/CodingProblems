# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(root, "")]
        
        result = set()
        while len(stack) > 0:
            current_node, current_path = stack.pop()
            
            
            if current_node != None:
                stack.append((current_node.left, current_path + str(current_node.val) + "->"))
                stack.append((current_node.right, current_path + str(current_node.val) + "->"))
                
                if current_node.left is None and current_node.right is None:
                    print(current_node.val)
                    result.add(current_path + str(current_node.val))

        return [item for item in result]

