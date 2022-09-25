class MyCircularQueue:

    def __init__(self, k: int):
        self.__items = [0 for i in range(k)]
        self.__amount_of_items = 0
        
        self.__front = 0
        self.__back = 0
        
        
    def enQueue(self, value: int) -> bool:
        if self.__amount_of_items == len(self.__items):
            return False
        
        self.__items[self.__back] = value
        self.__amount_of_items += 1
        
        self.__back += 1
        if self.__back == len(self.__items):
            self.__back = 0
        
        return True
    
    
    def deQueue(self) -> bool:
        if self.__amount_of_items == 0:
            return False
        
        self.__amount_of_items -= 1
        self.__front += 1
        
        if self.__front == len(self.__items):
            self.__front = 0
        
        return True
        

    def Front(self) -> int:
        if self.__amount_of_items == 0:
            return -1
        
        return self.__items[self.__front]
        

    def Rear(self) -> int:
        if self.__amount_of_items == 0:
            return -1
        
        return self.__items[self.__back - 1]
        

    def isEmpty(self) -> bool:
        return self.__amount_of_items == 0
        

    def isFull(self) -> bool:
        return self.__amount_of_items == len(self.__items)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

