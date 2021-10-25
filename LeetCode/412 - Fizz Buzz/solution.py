class Solution:
    def get_answer(self, index: int) -> str:
        if index % 3 == 0 and index % 5 == 0:
            return "FizzBuzz"
        elif index % 3 == 0 and index % 5 != 0:
            return "Fizz"
        elif index % 3 != 0 and index % 5 == 0:
            return "Buzz"
        else:
            return str(index)
        
    def fizzBuzz(self, n: int) -> List[str]:
        return [self.get_answer(i) for i in range(1, n+1)]

