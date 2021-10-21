class RandomizedSet:

    def __init__(self):
        self.items = {}
        self.indexes = {}
        self.free_indexes = [0]
        

    def insert(self, val: int) -> bool:
        if val not in self.items:
            free_index = self.free_indexes.pop()
            
            self.items[val] = free_index
            self.indexes[free_index] = val
            
            self.free_indexes.append(free_index + 1)
            
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            target_index = self.items[val]
            
            del self.items[val]
            del self.indexes[target_index]
            
            self.free_indexes.append(target_index)
            
            return True
        
        return False

    def getRandom(self) -> int:
        indexes = list(self.indexes.keys())
        
        random_number = random.randrange(len(indexes))
        
        return self.indexes[indexes[random_number]]

