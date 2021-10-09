class Node:
    def __init__(self, value: str):
        self.value = value
        self.children = []
        
    def add_child(self, value: str):
        new_child = Node(value)
        self.children.append(new_child)
    
    def get_child(self, c: str):
        children_letters = [(index, node.value) for index, node in enumerate(self.children)]
        
        if children_letters == [] or c not in [node[1] for node in children_letters]:
            return None
        else:
            target_index = -1
            for i, v in children_letters:
                if v == c:
                    target_index = i
                    break
            return self.children[target_index]
    def __str__(self) -> str:
        return self.value + str(self.children)
    
class Trie:
    def __init__(self):
        self.root = Node('-')
        
    def insert(self, word: str) -> None:
        current = self.root
        next_node = None
        for c in word:
            next_node = current.get_child(c)
            if next_node is None:
                current.add_child(c)
                next_node = current.children[-1]
                
            current = next_node
            next_node = None
            
        current.add_child('.')

    def search(self, word: str) -> bool:
        current = self.root
        next_node = None
        for c in word:
            next_node = current.get_child(c)
            if next_node is None:
                return False
            
            current = next_node
            next_node = None
        
        next_node = current.get_child('.')
        return next_node != None
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            next_node = current.get_child(c)
            
            if next_node is None:
                return False
            
            current = next_node
            next_node = None
            
        next_node = current.get_child('.')
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

