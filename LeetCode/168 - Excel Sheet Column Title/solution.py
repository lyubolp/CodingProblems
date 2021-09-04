class Solution:
    def convertIntToLetter(self, number: int) -> str:
        if number == 0:
            return 'Z'
        return chr(number + 64)
        
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 26:
            result += self.convertIntToLetter(columnNumber % 26)

            if columnNumber % 26 == 0:
                columnNumber = columnNumber // 26 - 1
            else:
                columnNumber = columnNumber // 26
            
        result += self.convertIntToLetter(columnNumber)
        
        return result[::-1]

