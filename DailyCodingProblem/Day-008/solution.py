"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

def is_unival_tree(root: Node) -> bool:
    stack = [root]

    target_val = root.val

    values = []

    while len(stack) > 0:
        current_node = stack.pop()

        if current_node == None:
            continue

        values.append(current_node.val)

        stack.append(current_node.left)
        stack.append(current_node.right)
    
    return all(value == target_val for value in values)


def get_count_of_unival_trees(root: Node) -> int:
    if root == None:
        return 0
    
    current_node = 1 if is_unival_tree(root) else 0
    return current_node + get_count_of_unival_trees(root.left) + get_count_of_unival_trees(root.right)

if __name__ == "__main__":
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    
    print(get_count_of_unival_trees(root))