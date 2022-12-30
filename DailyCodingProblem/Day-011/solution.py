"""
Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings,
    return all strings in the set that have s as a prefix.

For example, given the query string "de"
    and the set of strings [dog, deer, deal],
    return [deer, deal].
"""
from typing import List


class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children = []

def build_trie(strings: List[str]) -> Node:
    root = Node("")

    for string in strings:
        current = root
        for char in string:
            values = [node.value for node in current.children]

            if char in values:
                index = values.index(char)
                current = current.children[index]
            else:
                new_node = Node(char)
                current.children.append(new_node)
                current = new_node

    return root

def dfs(prefix: str, root: Node) -> List[str]:
    stack = [(child, prefix) for child in root.children]
    result = []

    while len(stack) > 0:
        node, current = stack.pop()
        current += node.value

        if len(node.children) == 0:
            result.append(current)
        else:
            for child in node.children:
                stack.append((child, current))

    return result

def autocomplete(query, strings):
    root = build_trie(strings)

    for char in query:
        for node in root.children:
            if node.value == char:
                root = node
                break
    
    return dfs(query, root)

if __name__ == "__main__":
    query = "de"
    strings = ["dog", "deer", "deal"]

    print(autocomplete(query, strings))