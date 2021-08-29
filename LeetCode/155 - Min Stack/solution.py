class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.items.append(val)
        
        if len(self.min) != 0:
            min_item = min(self.min[-1], val)
        else:
            min_item = val
            
        self.min.append(min_item)
        

    def pop(self) -> None:
        self.items.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]

